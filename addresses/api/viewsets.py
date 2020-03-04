from ..models import Address, City
from .serializers import AddressSerializer
from rest_framework import viewsets
from rest_framework import pagination
from django_filters import rest_framework as filters


class AddressPagination(pagination.PageNumberPagination):
    page_size = 1000


class CityFilter(filters.FilterSet):

    class Meta:
        model = City
        fields = {
                "name": ("icontains",),
                "code": ("exact",),
                }


class AddressFilter(filters.FilterSet):

    city = CityFilter()

    class Meta:
        model: Address
        fields = {
                "code": ("exact", ),
                "street": ("icontains",),
                "zipcode": ("exact", ),
                "house_number": ("exact", ),
                }


class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_class = AddressFilter
    pagination_class = AddressPagination

    http_method_names = ['get', 'head']
