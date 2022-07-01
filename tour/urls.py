from django.urls import path
from . views import tour, single_tour,CreateCheckoutSessionView, stripe_webhook,Review_model,booked_secessful, delete_booked_tour
                    

app_name = 'tour'
urlpatterns = [
    
    path('', tour, name='home'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
     
     
    path('success/', booked_secessful , name='success'),
    path('delete_booked_tour/<slug:review_slug>', delete_booked_tour , name='delete_booked_tour'),
    
    path('review/<slug:review_slug>', Review_model, name='review'),
     
    path('create-checkout-session/<slug:tour_slug>', CreateCheckoutSessionView, name='create-checkout-session'),
    path('<slug:tour_slug>',single_tour),
]