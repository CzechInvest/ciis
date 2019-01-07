from django.shortcuts import render
from .models import Address
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .models import Address

# Create your views here.

def address(request, address_id):
    address = Address.objects.get(pk=address_id)
    if not address:
        return HttpResponseNotFound()
    else:
        return HttpResponse("Address found")

def address_json(request, address_id):
    address = Address.objects.get(pk=address_id)
    return address.json

def address_search(request):
    pass

def address_search_json(request, query):
    addresses = Address.objects.find()
    pass
