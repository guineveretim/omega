from django.urls import path
from .views import (Home, create_booking, about
  )


urlpatterns = [
    #Home Url
    path('', Home, name='home'),
    path('booking/', create_booking, name='booking'),
    path('about/', about, name='about'),
    
]
