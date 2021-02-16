from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from ..ipstack_API import get_coordinates
from ..models import Geolocation
from .serializers import GeolocationSerializer
from rest_framework.response import Response

#  TODO:
#   1. View geolocation (from external API - not saved in DB) based on:
#       - ip
#       - url
#   3. Show geolocation from DB based on logged in user
#   2. Save geolocation in DB
#       - validation: user with this IP have already saved his geolocation?
#   3. Delete geolocation from DB
#       - only data of logged in user

# class GeolocationListView(generics.ListAPIView):
#     queryset = Geolocation.objects.all()
#     serializer_class = GeolocationSerializer


class GeolocationGetView(APIView):
    def get(self, request):
        return JsonResponse(get_coordinates())


class GeolocationDetailView(generics.RetrieveAPIView):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer

# class GeolocationCreate(generics.CreateAPIView):
