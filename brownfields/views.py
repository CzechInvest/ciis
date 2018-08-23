from django.shortcuts import render
from .models import Brownfield
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
import json


# Create your views here.
def index(request):
    data = {
        "brownfields": Brownfield.objects.all()
    }

    return render(request, 'brownfields/index.html', data)


def bfsjson(request):

    data = {
        "brownfields": [
            {
                "id": b.id,
                "title": b.title,
                "centroid": json.loads(b.location.geometry.centroid.json)
            } for b in Brownfield.objects.all()]
    }
    return JsonResponse(data)


def bfjson(request, bf):

    bf = Brownfield.objects.get(pk=bf)

    return JsonResponse(bf.json)
