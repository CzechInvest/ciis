from .models import Ai
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField


class AiSerializer(geoserializers.GeoFeatureModelSerializer):

    # a field which contains a geometry value and can be used as geo_field
    geom = GeometrySerializerMethodField()
    def get_geom(self, obj):
        return obj.address.coordinates

    class Meta:
        depth = 1
        model = Ai
        geo_field = "geom"
        fields = [
            "id",
            "name",
            "name_en",
            "url",
            "form",
            "address",
        ]