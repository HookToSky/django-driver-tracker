from random import randrange, random, uniform
import factory
from django.contrib.gis.geos import Point
from mapApp.models import Marker


class DriverFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = Marker
    driverName = factory.Faker('name')
    driverCityOrigin = factory.Faker('city')
    driverLanguage = ['de', 'en', 'nl', 'fr', 'es', 'ar'][randrange(6)]
    driverPhone = factory.Faker('phone_number')
    driverInfo = factory.Faker('catch_phrase')
    licensePlate = factory.Faker('license_plate')
    kmDriven = int(random() * 100000)
    location = Point(x=uniform(-180.0, 180.0), y=uniform(-90.0, 90.0), srid=4326)
    