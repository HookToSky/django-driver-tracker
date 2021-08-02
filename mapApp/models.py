#from django.db import models

# Create your models here.
from django.contrib.gis.db import models


class Marker(models.Model):
    """A marker with driver info and location."""

    driverName = models.CharField(max_length=255)
    driverCityOrigin = models.CharField(max_length=255)
    driverLanguage = models.CharField(max_length=255)
    driverPhone = models.CharField(max_length=255)
    driverInfo = models.CharField(max_length=255)
    licensePlate = models.CharField(max_length=255)
    kmDriven= models.IntegerField()
    location = models.PointField()

    def __str__(self):
        """Return string representation."""
        return self.driverName