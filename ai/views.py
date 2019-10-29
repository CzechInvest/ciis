from django.shortcuts import render
from .models import Ai
from .serializers import AiSerializer
from rest_framework import viewsets

class AiViewset(viewsets.ModelViewSet):
    queryset = Ai.objects.all()
    serializer_class = AiSerializer
    http_method_names = ["get", "head"]
