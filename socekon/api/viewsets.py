from ..models import HumanResourcesNuts3, HumanResourcesLau1, Date
from cigeo.models import Nuts3, Lau1
from .serializers import HRNuts3Serializer, HRLau1Serializer, HRNuts3NonGeomSerializer
from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework import pagination
from django_filters import rest_framework as filters
import calendar

class Nuts3Pagination(pagination.PageNumberPagination):
    page_size = 13

class Lau1Pagination(pagination.PageNumberPagination):
    page_size = 77

class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class MonthFilter(filters.CharFilter):

    def filter(self, qs, value):

        if value:
            try:
                year, month = (int(x) for x in value.split("-"))
                assert month <= 12
                assert year > 1918 and year < 2100
            except Exception as e:
                raise exceptions.ParseError("Month must be given in format YYYY-MM")

            last_day_of_month = calendar.monthrange(year, month)[1]
            value = f"{year}-{month}-{last_day_of_month}"

        return super().filter(qs, value)

class HRNuts3Filter(filters.FilterSet):

    date__date = MonthFilter()
    nuts3__code = NumberInFilter(field_name='nuts3__code', lookup_expr='in')
    id = NumberInFilter(field_name='pk', lookup_expr='in')

    class Meta:
        model = HumanResourcesNuts3
        fields = {
                "nuts3__name": ("icontains",),
                }

class HRLau1Filter(filters.FilterSet):

    date__date = MonthFilter()
    lau1__code = NumberInFilter(field_name='lau1__code', lookup_expr='in')
    id = NumberInFilter(field_name='pk', lookup_expr='in')

    class Meta:
        model = HumanResourcesLau1
        fields = {
                "lau1__name": ("icontains",),
                }


class Nuts3ViewSet(viewsets.ModelViewSet):
    basename="socekon/nuts3"

    queryset = HumanResourcesNuts3.objects.all().order_by("-date").prefetch_related("date").prefetch_related("nuts3")
    filter_class = HRNuts3Filter
    pagination_class = Nuts3Pagination


    http_method_names = ['get', 'head']

    def get_serializer_class(self):

        if self.get_serializer_context()["format"] == "xlsx":
            self.filename = 'nuts3.xlsx'
            return HRNuts3NonGeomSerializer
        else:
            return HRNuts3Serializer

class Lau1ViewSet(viewsets.ModelViewSet):
    queryset = HumanResourcesLau1.objects.all().order_by("-date").prefetch_related("date").prefetch_related("lau1")
    serializer_class = HRLau1Serializer
    filter_class = HRLau1Filter
    pagination_class = Lau1Pagination

    http_method_names = ['get', 'head']
