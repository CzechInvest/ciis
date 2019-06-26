from django.shortcuts import render
from .models import Nuts3
from django.http import JsonResponse
import json

def nuts3_json(request):

    data = {
        "type": "FeatureCollection",
        "features": [{
            "properties": {
                "name": n.name,
                "code": n.code
            },
            "geometry": json.loads(n.geometry.geojson)
        } for n in Nuts3.objects.all()
        ]
    }

    return JsonResponse(data)

def lau1_json(request):

    data = {
        "type": "FeatureCollection",
        "features": [{
            "properties": {
                "name": l.name,
                "code": l.code
            },
            "geometry": json.loads(l.geometry.geojson)
        } for l in Lau1.objects.all()
        ]
    }

    return JsonResponse(data)

