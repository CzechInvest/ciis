from ..models import Vtp, VtpType, Service
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
import rest_pandas


from addresses.api import serializers as address_serializer


class ServiceListSerializer(serializers.ListSerializer):

    def to_representation(self, value):
        return "; ".join((s["service"] for s in value.values()))

class TypeListSerializer(serializers.ListSerializer):

    def to_representation(self, value):
        return "; ".join((v["type"] for v in value.values()))

class AddressSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return str(value)

class NonGeomSerializer(serializers.ModelSerializer):

    services = ServiceListSerializer(child=serializers.StringRelatedField(many=True), many=False)
    type = TypeListSerializer(child=serializers.StringRelatedField(many=True))

    address = AddressSerializer()

    class Meta:
        model = Vtp
        fields = ['pk', 'name', 'type', "url", "services", "address"]

class VtpSerializer(geoserializers.GeoFeatureModelSerializer):

    services = serializers.StringRelatedField(many=True, read_only=True)
    type = serializers.StringRelatedField(many=True)

    geom = GeometrySerializerMethodField()
    # address = serializers.CharField()
    address = address_serializer.AddressAsTextSerializer()

    def get_geom(self, vtp):
        return vtp.address.coordinates

    class Meta:
        model = Vtp
        #list_serializer_class = rest_pandas.PandasSerializer
        geo_field = "geom"
        fields = ['name', 'type', "url", "services", "address"]
