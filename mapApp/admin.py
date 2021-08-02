#from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin

from mapApp.models import Marker


@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("driverName", "location")