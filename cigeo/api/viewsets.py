from ..models import Nuts3, Lau1
from .serializers import Nuts3Serializer, Lau1Serializer
from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework import pagination
from django_filters import rest_framework as filters

class Nuts3Filter(filters.FilterSet):

    class Meta:
        model = Nuts3
        fields = {
                "name": ("icontains",),
                "code": ("exact",),
                }

class Lau1Filter(filters.FilterSet):

    class Meta:
        model = Lau1
        fields = {
                "name": ("icontains",),
                "code": ("exact",),
                }


class Nuts3ViewSet(viewsets.ModelViewSet):
    queryset = Nuts3.objects.all()
    serializer_class = Nuts3Serializer
    filter_class = Nuts3Filter

    http_method_names = ['get', 'head']

class Lau1ViewSet(viewsets.ModelViewSet):
    queryset = Lau1.objects.all()
    serializer_class = Lau1Serializer
    filter_class = Lau1Filter

    http_method_names = ['get', 'head']
