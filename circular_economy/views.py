from django.shortcuts import render
from .models import Company
from .serializers import CompanySerializer
from rest_framework import viewsets

class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ["get", "head"]
