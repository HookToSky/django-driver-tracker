import math
from random import random
from datetime import timedelta
from django.contrib.gis.geos import Point
from celery import periodic_task
from .models import Marker

@periodic_task(run_every=timedelta(seconds=5))
def update_driver_locations():
    print('Updating driver data locations in the database ...')
    updateDrivers()
     

def updateDrivers():
    markers = Marker.objects.all()
    drivers = markers["features"]
    for driver in drivers:
        current_location = driver["geometry"]["coordinates"]
        new_latitude, new_longitude = updatePositions(current_location[0], current_location[1])
        new_location = Point(x=new_longitude, y=new_latitude, srid=4326)
        print('updating:   ', driver.driverName)
        Marker.objects.filter(driverName=driver.driverName).update(location = new_location)

def updatePositions(x0, y0):
    radiusInDegrees = 500000 / 111000 # radius is 500km
    u = random()
    v = random()
    w = radiusInDegrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)

    new_x = x / math.cos(math.radians(y0))
    new_longitude = new_x + x0
    new_latitude = y + y0
    return {new_latitude, new_longitude}
