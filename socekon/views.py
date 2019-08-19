from django.shortcuts import render
from cigeo.views import MapView
from .models import Nuts3Stats, Lau1Stats
import csv
from ciis.views import IndexView as CIISIndexView
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import Nuts3Serializer
from .serializers import Lau1Serializer


class IndexView(CIISIndexView):
    template_name = "socekon/index.html"


class MapViewNuts3(MapView):
    model = Nuts3Stats
    context_object_name = "data"

class MapViewLau1(MapView):
    model = Lau1Stats
    context_object_name = "data"


class Nuts3ViewSet(viewsets.ModelViewSet):
    queryset = Nuts3Stats.objects.all()
    serializer_class = Nuts3Serializer
    http_method_names = ['get', 'head']


class Lau1ViewSet(viewsets.ModelViewSet):
    queryset = Lau1Stats.objects.all()
    serializer_class = Lau1Serializer
    http_method_names = ['get', 'head']

