from django.urls import path
from . import views

urlpatterns = [
    path('geolocation/',
         views.GeolocationGetView.as_view(),
         name='geolocation_list'),
    path('geolocation/<pk>/',
         views.GeolocationDetailView.as_view(),
         name='geolocation_detail')
]