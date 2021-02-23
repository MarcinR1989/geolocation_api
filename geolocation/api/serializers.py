from rest_framework import serializers
from ..models import Geolocation
from django.contrib.auth.models import User


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ('id', 'ip', 'latitude', 'longitude', 'created_at')
