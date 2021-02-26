from django.shortcuts import render

# Create your views here.
from django.urls import path
from cigeo.views import MapView
from .models import RK

class MapRK(MapView):
    model = RK
    context_object_name = "data"
