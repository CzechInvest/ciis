from ..models import RK
from .serializers import RKSerializer
from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework import pagination
from django_filters import rest_framework as filters

class RKFilter(filters.FilterSet):

    class Meta:
        model = RK
        fields = {
                "name": ("icontains",),
                "address__adm": ("exact",),
                }

class RKViewSet(viewsets.ModelViewSet):
    queryset = RK.objects.all()
    serializer_class = RKSerializer
    filter_class = RKFilter

    http_method_names = ['get', 'head']

    def get_serializer_class(self):

        if self.get_serializer_context()["format"] == "xlsx":
            self.filename = 'rks.xlsx'
            return NonGeomSerializer
        else:
            return RKSerializer
