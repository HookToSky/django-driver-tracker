"""Marker serializers."""

from rest_framework_gis import serializers

from mapApp.models import Marker


class MarkerSerializer(serializers.GeoFeatureModelSerializer):
    """Marker GeoJSON serializer."""

    class Meta:
        """Marker serializer meta class."""

        fields = ("id", "driverName", "driverCityOrigin", "driverLanguage", "driverPhone", "driverInfo", "licensePlate", "kmDriven")
        geo_field = "location"
        model = Marker