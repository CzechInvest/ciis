from django.shortcuts import render
from cigeo.views import MapView
from .models import Nuts3Stats, Lau1Stats, HumanResourcesNuts3, HumanResourcesLau1, Date
import csv
from ciis.views import IndexView as CIISIndexView
from rest_framework import viewsets
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
#from .serializers import Nuts3Serializer
#from .serializers import Lau1Serializer
#from .serializers import HRNuts3Serializer
#from .serializers import HRLau1Serializer
#from .serializers import DateSerializer
#from .serializers import DateDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import calendar


class IndexView(CIISIndexView):
    template_name = "socekon/index.html"


class MapViewNuts3(MapView):
    model = Nuts3Stats
    context_object_name = "data"

class MapViewLau1(MapView):
    model = Lau1Stats
    context_object_name = "data"


#class Nuts3ViewSet(viewsets.ModelViewSet):
#    queryset = Nuts3Stats.objects.all()
#    serializer_class = Nuts3Serializer
#    http_method_names = ['get', 'head']
#
#
#class Lau1ViewSet(viewsets.ModelViewSet):
#    queryset = Lau1Stats.objects.all()
#    serializer_class = Lau1Serializer
#    http_method_names = ['get', 'head']
#
#
#
#class HRLau1ViewList(generics.ListAPIView):
#
#    serializer_class = HRLau1Serializer
#
#    def get_queryset(self):
#        """
#        This view should return a list of all the purchases for
#        the user as determined by the username portion of the URL.
#        """
#        year = self.kwargs['year']
#        month = self.kwars['month']
#        print("#####", month, year)
#        return HumanResourcesLau1.objects.all() # filter(purchaser__username=username)
#
#class DateViewSet(viewsets.ViewSet):
#    def list(self, request):
#        queryset = Date.objects.all()
#        serializer = DateSerializer(queryset, many=True)
#        return Response(serializer.data)
#
#    def get_object(self):
#        queryset = self.filter_queryset(self.get_queryset())
#        year, month = self.kwargs["month"].split("-")
#        last_day = calendar.monthrange(int(year),int(month))[1]
#
#        date = get_object_or_404(queryset, date=f"{year}-{month}-{last_day}")
#
#        return date
