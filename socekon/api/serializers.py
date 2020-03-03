from ..models import Nuts3Stats, Lau1Stats, HumanResourcesNuts3, HumanResourcesLau1, Date
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField


class Nuts3Serializer(serializers.HyperlinkedModelSerializer, geoserializers.GeoFeatureModelSerializer):

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

    lau1_name = serializers.CharField(source='lau1.name')
    lau1_code = serializers.CharField(source='lau1.code')


    # a field which contains a geometry value and can be used as geo_field
    geom = GeometrySerializerMethodField()
    def get_geom(self, obj):
        return obj.lau1.geometry

    class Meta:
        model = HumanResourcesLau1
        lookup_field = 'month'
        geo_field = "geom"
        fields = [
                  "date",
                  "lau1_name",
                  "lau1_code",
                  "inhabitans",
                  "productive_inhabitans",
                  "unemployed",
                  "vacancies",
                  "unemployment",
                  "applications_per_vacancy"
                  ]

class DateSerializer(serializers.HyperlinkedModelSerializer):

    default_fields = ('month',)                                                                        

    class Meta:
        model = Date
        fields = ["month"]
        lookup_field = 'month'
        read_only_fields = ["date"]

class DateDetailSerializer(serializers.HyperlinkedModelSerializer):

    default_fields = ('month',)                                                                        

    class Meta:
        model = Date
        fields = ["month", "czk_usd", "czk_euro"]
        lookup_field = 'month' # This does not work                                                                      
        read_only_fields = ["date"]
