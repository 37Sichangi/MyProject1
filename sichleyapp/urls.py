from django.urls import path, include

from .views import *


urlpatterns= [
  
  path( '',Home.as_view(), name='home'),
  path( 'customer/',Customer.as_view(), name='cust-page'),
  path('region/', Region.as_view(), name='region' ),
  path('land/' ,Land.as_view(), name='land'),

  ]