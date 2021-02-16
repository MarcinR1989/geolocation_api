from django.contrib import admin

from geolocation.models import Geolocation


@admin.register(Geolocation)
class GeolocationAdmin(admin.ModelAdmin):
    pass
