import math
from random import random
from django.contrib.gis.geos import Point
import celery
from .models import Marker

@celery.task(name = 'update_driver_locations')
def update_driver_locations():
    print('Updating driver data locations in the database ...')
    drivers = list(Marker.objects.all())
    for driver in drivers:
        driverLoc= driver.location
        current_location = [coord for coord in driverLoc]
        new_longitude, new_latitude = updatePositions(current_location[0], current_location[1])
        new_location = Point(x=new_longitude, y=new_latitude, srid=4326)
        print('updating:   ', driver.driverName, 'with new location coordinates ', new_location)
        Marker.objects.filter(driverName=driver.driverName).update(location = new_location)
     

def updatePositions(x0, y0):
    radiusInDegrees = 100000 / 111000 # radius is 100km
    u = random()
    v = random()
    w = radiusInDegrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)

    new_x = x / math.cos(math.radians(y0))
    new_longitude = new_x + x0
    new_latitude = y + y0
    return {new_longitude, new_latitude}
