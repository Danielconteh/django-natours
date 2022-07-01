from django.urls import path
from django.views.generic import TemplateView
from . views import tour, single_tour,CreateCheckoutSessionView, stripe_webhook,Review_model,booked_secessful
                    

app_name = 'tour'
urlpatterns = [
    path('', tour, name='home'),
     path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', TemplateView.as_view(template_name='cancel.html') , name='cancel'),
    path('success/', booked_secessful , name='success'),
    path('review/<slug:review_slug>', Review_model, name='review'),
     
    path('create-checkout-session/<slug:tour_slug>', CreateCheckoutSessionView, name='create-checkout-session'),
    path('<slug:tour_slug>',single_tour),
]