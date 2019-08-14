from .models import Nuts3, Lau1
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class Nuts3Serializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = Nuts3
        geo_field = "geometry"
        fields = ['code', 'name']

class Lau1Serializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = Lau1
        geo_field = "geometry"
        fields = ['code', 'name']
