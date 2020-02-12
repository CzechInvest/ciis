from .models import Address
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class AddressSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = Address
        geo_field = "coordinates"
        fields = ['adm', 'street', "house_number", "orientation_number",
                  "city", "zipcode"]


class TextAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields: ["adm", "street", "house_number", "orientation_number", "city",
                "zipcode"]
