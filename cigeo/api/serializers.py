from ..models import Nuts3, Lau1
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField


class Nuts3Serializer(geoserializers.GeoFeatureModelSerializer):

    geom = GeometrySerializerMethodField()

    def get_geom(self, obj):
        return obj.geometry

    class Meta:
        model = Nuts3
        geo_field = "geom"
        fields = ("name", "code")


class Lau1Serializer(geoserializers.GeoFeatureModelSerializer):

    geom = GeometrySerializerMethodField()

    def get_geom(self, obj):
        return obj.geometry

    class Meta:
        model = Lau1
        geo_field = "geom"
        fields = ("name", "code")
