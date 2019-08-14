from django.shortcuts import render
from .models import Nuts3, Lau1
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from ciis.views import IndexView as CIISIndexView
from rest_framework import viewsets
from .serializers import Nuts3Serializer, Lau1Serializer

import json

class IndexView(CIISIndexView):
    template_name = "cigeo/index.html"

class MapView(ListView):
    template_name = None # fill this in your class
    model = None # fill this in your class
    context_object_name = None # Providing a useful context_object_name is always a good idea. Your coworkers who design templates will thank you.

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        #context['geojson'] = json.dumps({
        #    "type": "FeatureCollection",
        #    "features": [
        #        o.json for o in self.model.objects.all()
        #    ]})
        return context


class Nuts3ViewSet(viewsets.ModelViewSet):
    queryset = Nuts3.objects.filter(pk__lt=100)
    serializer_class = Nuts3Serializer
    http_method_names = ['get', 'head']


class Lau1ViewSet(viewsets.ModelViewSet):
    queryset = Lau1.objects.filter()
    serializer_class = Lau1Serializer
    http_method_names = ['get', 'head']


class NUTS3View(MapView):
    template_name = "cigeo/nuts3.html"
    model = Nuts3
    context_object_name = "data"


class LAU1View(MapView):
    template_name = "cigeo/lau1.html"
    model = Lau1
    context_object_name = "data"


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


def index(request):
    context = {
        "user":  request.user
    }
    return render(request, 'cigeo/index.html', context)
