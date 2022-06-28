from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

import json
from django.conf import settings
from django.dispatch import receiver
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Tour, Images, User_Image, Review
import datetime
import random
# from allauth.socialaccount.signals import pre_social_login
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt 
import stripe
from django.contrib import messages
from django.db.models import Avg





@receiver(user_signed_up)
def link_to_local_user(sender, request, user, **kwargs):    
    image = kwargs['sociallogin'].account.extra_data['picture']
    email_address =  kwargs['sociallogin'].account.extra_data['email']
    
    user = User.objects.filter(email=email_address)
   
    if user.exists():
        user_img = User_Image.objects.filter(user__email = email_address)
                
        if(user_img.exists() and user_img[0].image):return 
        
        user_img = User_Image(user=user[0], image=image)
        user_img.save()

      



# Create your views here.


# ALL TOURS

def tour(request):
    
    bannerImage = []
    data = Tour.objects.all()
    for index, _ in enumerate(data):
        data[index].startDates = datetime.datetime.fromisoformat(data[index].startDates[0].split('T')[0]).strftime(
            "%d %B %Y")
        bannerImage.append(data[index].coverImage)

    banner = bannerImage[random.randrange(0, len(data))]
    
    return render(request, 'tour.html', {'data': data, 'banner': banner, 'bannerImage': bannerImage})





# SIGNLE TOUR 


def single_tour(request, tour_slug):
    
    # try: data = Tour.objects.get(slug=tour_slug)
    # except ObjectDoesNotExist: return redirect('home')
    data = get_object_or_404(Tour,slug=tour_slug)

    next_date = datetime.datetime.fromisoformat(data.startDates[0].split('T')[0]).strftime("%B %Y")

    coords = data.location[0]["coordinates"]

    img = Images.objects.filter(post__pk=data.id)

    imgs,locationDes, locationCoords, locationDay, review = [], [], [], [],[]
    
    for images in img: imgs.append(images.images)

    locations, par_info = data.location, [data.description]

    par_description = [y for x in par_info for y in x.split('.\\n')]

    for item in locations:
        locationDes.append(item['description'])
        locationDay.append(item['day'])
        locationCoords.append(item['coordinates'])

    startLocation = data.startLocation.coordinates
    
    
    # ADD REVIEWS TO TAST!
    review_tour = Review.objects.filter(tour=tour_slug)
    if review_tour.exists():
        for index,_ in enumerate(review_tour):
            review_user = User_Image.objects.filter(user__email=review_tour[index].user) 
            
            review.append({"review_text":review_tour[index].review, 
                           'rating':float(review_tour[index].rating),
                           'image': review_user[0].image or review_user[0].photo ,
                           'name':review_user[0].user.first_name+ ' ' + review_user[0].user.last_name,
                          })
           
    # updating data ratingAvg for any single tour  [no rating yet!]
     # updating data ratingAvg for any single tour  [no rating yet!]
    if type(review_tour.aggregate(Avg('rating'))['rating__avg']) is type(None): 
        data.ratingAvg = 0
        data.save()
    
    else: 
        data.ratingAvg = float(review_tour.aggregate(Avg('rating'))['rating__avg'])
        data.save();
      
        
       
    return render(request, 'single_tour.html',
                  {'data': data, 'next_date': next_date, 'imgs': imgs, 'coords': coords, 'locationDes': locationDes,
                   'locationCoords': locationCoords, 'locationDay': json.dumps(locationDay),
                   'startLocation': startLocation, 'par_description': par_description, 'review':review})






# REVIEW LOGIC
def Review_model(request, review_slug):
    if not request.user.is_authenticated:
        messages.error(request, 'user must be login to write a review!')
        return redirect('/{}'.format(request.build_absolute_uri().split('/')[-1]))

        
    if not request.POST['review']:
        messages.warning(request, 'please write something!')
        return redirect('/{}'.format(request.build_absolute_uri().split('/')[-1]))

    rating = request.POST['rating'] or 0
    print(rating)
    data = Review(tour=review_slug,user=request.user.email,review=request.POST['review'],
                  rating=float(rating),time_posted=datetime.datetime.now())
    try:
        data.save()
    except IntegrityError:
        messages.warning(request, 'you have already write review for  this tour!!')
        print('hello')
        return redirect('/{}'.format(request.build_absolute_uri().split('/')[-1]))
    
    return redirect('/{}'.format(request.build_absolute_uri().split('/')[-1]))


    




# 901687663123-e0s0dtfarnr0d9e3u9bc6fbvkr8tii7h.apps.googleusercontent.com
# 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










# CHECKOUT SESSION

def CreateCheckoutSessionView(request, tour_slug):
    if not request.user.is_authenticated:
        return redirect('tour')
        
    data = Tour.objects.filter(slug=tour_slug)[0]
    
    print(data)
    
    # if not data.exists():
    #     return HttpResponse('not found!!')
        
    print("============================")
  
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    YOUR_DOMAIN = 'http://localhost:8000/'
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': data.price * 100,
                    'product_data': {
                        'name': data.name,
                        
                        # 'images': ['https://i.imgur.com/EHyR2nP.png'] {{product.coverImage}},
                    },
                },
                'quantity': 1,
            },
        ],
         metadata={
                "tour_slug": data.slug,
                "price": data.price,
                "email": request.user.email,
                
            },
        mode='payment',
        success_url= YOUR_DOMAIN + 'success/',
        cancel_url= YOUR_DOMAIN + 'cancel/',
    )
    return redirect(checkout_session.url, code=303)





# STRIPE stripe_webhook
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET_KEY
@csrf_exempt
def stripe_webhook(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)



 # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
      session = event['data']['object']
      print(session)

    #   customer_email = session["customer_details"]["email"]
    #   product_id = session["metadata"]["product_id"]

    #   product = Product.objects.get(id=product_id)

  # Passed signature verification
  return HttpResponse(status=200)
    
    
    
    
    
    
    
    
    
    
    
    
    
    # ERROR HANDLING
    
def handler_404(request, *args, **argv):
    return render(request,'not_found.html')

def handler500(request,*args, **argv):
    return render(request,'Server_Error.html')
    