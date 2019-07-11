from django.shortcuts import render
from cigeo.views import MapView
from .models import Nuts3Stats, Lau1Stats
import csv
from django.http import HttpResponse, JsonResponse


class MapViewNuts3(MapView):
    model = Nuts3Stats
    context_object_name = 'nuts3'

class MapViewLau1(MapView):
    model = Lau1Stats
    context_object_name = 'nuts3'

def lau1_json(request):

    data = {
        "type": "FeatureCollection",
        "features": [o.json for o in Lau1Stats.objects.all()]
    }

    return JsonResponse(data)

def lau1_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="nuts3-socekon.csv"'

    writer = csv.writer(response)
    writer.writerow([prop for prop in Lau1Stats.objects.all()[0].json["properties"]])
    for lau1 in Lau1Stats.objects.all():
        writer.writerow([lau1.json["properties"][prop] for prop in lau1.json["properties"]])

    return response


def nuts3_json(request):

    data = {
        "type": "FeatureCollection",
        "features": [o.json for o in Nuts3Stats.objects.all()]
    }

    return JsonResponse(data)

def nuts3_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="nuts3-socekon.csv"'

    writer = csv.writer(response)
    writer.writerow([prop for prop in Nuts3Stats.objects.all()[0].json["properties"]])
    for nut3 in Nuts3Stats.objects.all():
        writer.writerow([nut3.json["properties"][prop] for prop in nut3.json["properties"]])

    return response

