from django.urls import path
from django.views.generic import TemplateView
from . views import tour, single_tour,CreateCheckoutSessionView, stripe_webhook,Review_model
                    

app_name = 'tour'
urlpatterns = [
    path('', tour, name='home'),
     path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
     path('review/<slug:review_slug>', Review_model, name='review'),
     
    path('create-checkout-session/<slug:tour_slug>', CreateCheckoutSessionView, name='create-checkout-session'),
    path('<slug:tour_slug>',single_tour),
]