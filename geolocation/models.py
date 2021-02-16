from django.db import models


# Create your models here.
class Geolocation(models.Model):
    ip_address = models.CharField(max_length=64)
    latitude = models.CharField(max_length=64)
    longitude = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #  TODO:
    #  user?
