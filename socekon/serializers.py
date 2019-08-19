from .models import Nuts3Stats, Lau1Stats
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField


class Nuts3Serializer(geoserializers.GeoFeatureModelSerializer):

    nuts3_name = serializers.CharField(source='nuts3.name')
    nuts3_code = serializers.CharField(source='nuts3.code')

    # a field which contains a geometry value and can be used as geo_field
    geom = GeometrySerializerMethodField()
    def get_geom(self, obj):
        return obj.nuts3.geometry

    class Meta:
        model = Nuts3Stats
        geo_field = "geom"
        fields = ['nuts3_code', 'nuts3_name', "population", "work_power", "unemployment",
                  "unemployment_rate", "unemployed_per_job", "medium_salary"]


class Lau1Serializer(geoserializers.GeoFeatureModelSerializer):

    geom = GeometrySerializerMethodField()
    def get_geom(self, obj):
        return obj.lau1.geometry

    lau1_name = serializers.CharField(source='lau1.name')
    lau1_code = serializers.CharField(source='lau1.code')

    class Meta:
        model = Lau1Stats
        geo_field = "geom"
        fields = ['lau1_code', 'lau1_name', "population", "work_power", "unemployment",
                  "unemployment_rate", "unemployed_per_job"]
