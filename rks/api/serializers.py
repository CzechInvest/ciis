from ..models import RK
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from addresses.api import serializers as address_serializer

class AddressSerializer(geoserializers.ModelSerializer):

    def to_representation(self, value):
        return str(value)


class NonGeomSerializer(geoserializers.ModelSerializer):

    address = AddressSerializer()

    class Meta:
        model = RK
        fields = ['pk', 'name', 'director', "email", "phone", "address"]


class RKSerializer(geoserializers.GeoFeatureModelSerializer):

    geom = GeometrySerializerMethodField()
    address = address_serializer.AddressAsTextSerializer()

    def get_geom(self, obj):
        return obj.address.geometry

    class Meta:
        model = RK
        geo_field = "geom"
        fields = ("name", "director", "address", "email", "phone")
