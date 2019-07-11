from django.shortcuts import render
from .models import Nuts3
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
import json

class MapView(ListView):
    template_name = None # fill this in your class
    model = None # fill this in your class
    context_object_name = None # Providing a useful context_object_name is always a good idea. Your coworkers who design templates will thank you.

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of all the books
        context['geojson'] = json.dumps({
            "type": "FeatureCollection",
            "features": [
                o.json for o in self.model.objects.all()
            ]})
        return context

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

