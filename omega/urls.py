from django.urls import path
from .views import (Home, create_booking, about, services, contact, pricacy_policy
  )


urlpatterns = [
    #Home Url
    path('', Home, name='home'),
    path('booking/', create_booking, name='booking'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'), 
    path('privacy-policy/', pricacy_policy, name='privacy_policy'),
    
]
