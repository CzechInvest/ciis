from ..models import Address
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers

class AddressAsTextSerializer(serializers.ModelSerializer):

    text_address = serializers.CharField(source="__str__")

    class Meta:
        model = Address
        fields = ['adm', 'text_address']

class AddressSerializer(geoserializers.GeoFeatureModelSerializer):
    city = serializers.CharField(source="city.name")
    city_code = serializers.CharField(source="city.code")
    administrative_id = serializers.IntegerField(source="adm")

    class Meta:
        model = Address
        geo_field = "coordinates"
        fields = ['adm', 'administrative_id', 'street', "house_number", "orientation_number",
                  "city", "city_code", "zipcode"]
