from ..models import HumanResourcesNuts3, HumanResourcesLau1, Date
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField

class HRNuts3NonGeomSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='nuts3.name')
    code = serializers.IntegerField(source='nuts3.code')
    date = serializers.DateField(source='date.date')

    class Meta:
        model = HumanResourcesNuts3
        fields = [
                  "date",
                  "name",
                  "code",
                  "wages",
                  "inhabitans",
                  "productive_inhabitans",
                  "unemployed",
                  "vacancies",
                  "unemployment",
                  "applications_per_vacancy"
                  ]

class HRNuts3Serializer(geoserializers.GeoFeatureModelSerializer):
#class HRNuts3Serializer(serializers.ModelSerializer):

    name = serializers.CharField(source='nuts3.name')
    code = serializers.IntegerField(source='nuts3.code')
    date = serializers.DateField(source='date.date')

    geom = GeometrySerializerMethodField()

    def get_geom(self, obj):
        return obj.nuts3.geometry

    class Meta:
        model = HumanResourcesNuts3
        geo_field = "geom"
        fields = [
                  "date",
                  "name",
                  "code",
                  "wages",
                  "inhabitans",
                  "productive_inhabitans",
                  "unemployed",
                  "vacancies",
                  "unemployment",
                  "applications_per_vacancy"
                  ]

class HRLau1Serializer(geoserializers.GeoFeatureModelSerializer):

    name = serializers.CharField(source='lau1.name')
    code = serializers.IntegerField(source='lau1.code')
    date = serializers.DateField(source='date.date')

    geom = GeometrySerializerMethodField()

    def get_geom(self, obj):
        return obj.lau1.geometry

    class Meta:
        model = HumanResourcesLau1
        lookup_field = 'month'
        geo_field = "geom"
        fields = [
                  "date",
                  "name",
                  "code",
                  "inhabitans",
                  "productive_inhabitans",
                  "unemployed",
                  "vacancies",
                  "unemployment",
                  "applications_per_vacancy"
        ]
