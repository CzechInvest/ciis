from .models import Municipality, Company, Pilot
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField


class MunicipalitySerializer(geoserializers.GeoFeatureModelSerializer):

    # a field which contains a geometry value and can be used as geo_field
    geom = GeometrySerializerMethodField()
    def get_geom(self, obj):
        return obj.address.geometry

    class Meta:
        depth = 1
        model = Municipality
        geo_field = "geom"
        fields = [
            "uuid",
            "name",
            "activity",
            "url",
            "contact_person",
            "address"
            "characteristics",
            "project_description",
            "challange",
            "result",
            "keywords"
        ]
