from ..models import Address
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class AddressSerializer(geoserializers.GeoFeatureModelSerializer):
    city = serializers.CharField(source="city.name")
    city_code = serializers.CharField(source="city.code")

    class Meta:
        model = Address
        geo_field = "coordinates"
        fields = ['adm', 'street', "house_number", "orientation_number",
                  "city", "city_code", "zipcode"]
