from ..models import Vtp
from .serializers import VtpSerializer, NonGeomSerializer
from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework import pagination
from django_filters import rest_framework as filters

from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

class VtpFilter(filters.FilterSet):

    class Meta:
        model = Vtp
        fields = {
                "name": ("icontains",),
                "type__type": ("exact",),
                "services__service": ("exact",),
                "address__adm": ("exact",),
                }

class VtpViewSet(XLSXFileMixin, viewsets.ModelViewSet):
    queryset = Vtp.objects.all()
    filter_class = VtpFilter
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer, XLSXRenderer ]


    def get_serializer_class(self):

        if self.get_serializer_context()["format"] == "xlsx":
            self.filename = 'vtp.xlsx'
            return NonGeomSerializer
        else:
            return VtpSerializer

    http_method_names = ['get', 'head']

#class VtpPandasViewSet(PandasViewSet):
#
#    queryset = Vtp.objects.all()
#    serializer_class = VtpPandasSerializer
#
#    filter_class = VtpFilter
#
#    http_method_names = ['get', 'head']
