from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from geolocation.api.views import signup
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('geolocation/',
         views.GeolocationListCreate.as_view(),
         name='geolocation_list_create'),
    path('geolocation/now/',
         views.GeolocationActual.as_view(),
         name='geolocation_actual'),
    path('geolocation/<int:pk>/',
         views.GeolocationDelete.as_view(),
         name='geolocation_delete'),
    path('token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', auth_views.LoginView.as_view(
        redirect_field_name='geolocation_list_create'), name='login'),
    path('logout/', auth_views.LogoutView.as_view()),
    path('signup/', signup, name='signup'),

]

