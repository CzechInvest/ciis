from django.shortcuts import render
from .models import Municipality
from .serializers import MunicipalitySerializer
from rest_framework import viewsets

class MunicipalityViewset(viewsets.ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    http_method_names = ["get", "head"]
