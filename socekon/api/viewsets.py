from ..models import HumanResourcesNuts3, Date
from cigeo.models import Nuts3
from .serializers import HRNuts3Serializer
from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework import pagination
from django_filters import rest_framework as filters
import calendar

class Nuts3Pagination(pagination.PageNumberPagination):
    page_size = 14

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

    class Meta:
        model = HumanResourcesNuts3
        fields = {
                "nuts3__name": ("icontains",),
                "nuts3__code": ("exact",),
                }


class Nuts3ViewSet(viewsets.ModelViewSet):
    queryset = HumanResourcesNuts3.objects.all()
    serializer_class = HRNuts3Serializer
    filter_class = HRNuts3Filter
    pagination_class = Nuts3Pagination

    http_method_names = ['get', 'head']
