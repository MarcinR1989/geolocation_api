from django.db import models
from django.conf import settings


# Create your models here.


class Geolocation(models.Model):
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip = models.CharField(max_length=64)
    latitude = models.CharField(max_length=64)
    longitude = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f'{self.user_name}, {self.created_at}'
