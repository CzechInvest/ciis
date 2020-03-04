from .models import Vtp, VtpType, Service
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField


class VtpSerializer(geoserializers.GeoFeatureModelSerializer):

    services = serializers.StringRelatedField(many=True, read_only=True)
    type = serializers.StringRelatedField(many=True)

    # a field which contains a geometry value and can be used as geo_field
    geom = GeometrySerializerMethodField()
    address =  serializers.CharField()



    def get_geom(self, vtp):
        return vtp.address.coordinates

    class Meta:
        model = Vtp
        geo_field = "geom"
        fields = ['name', 'type', "url", "services", "address"]
