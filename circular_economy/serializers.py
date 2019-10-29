from .models import Municipality, Company, Pilot
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField


class CompanySerializer(geoserializers.GeoFeatureModelSerializer):

    # a field which contains a geometry value and can be used as geo_field
    geom = GeometrySerializerMethodField()
    def get_geom(self, obj):
        return obj.address.coordinates

    class Meta:
        depth = 1
        model = Company
        geo_field = "geom"
        fields = [
            "id",
            "name",
            "url",
            "contact_person",
            "address",
            "characteristics",
        ]
