from django.shortcuts import render
from .models import Address
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .serializers import AddressSerializer
from rest_framework import viewsets
from django.views.generic import ListView
#from rest_framework import mixins

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer = AddressSerializer
    http_method_names = ['get', 'head']

class AddressView(ListView):
    template_name = "addresses/address_list.html"
    model = Address # fill this in your class
    context_object_name = "data" # Providing a useful context_object_name is always a good idea. Your coworkers who design templates will thank you.
    paginate_by = 100  # if pagination is desired

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    return context
