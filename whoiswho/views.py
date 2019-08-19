from django.shortcuts import render
from .models import WhoIsWho
from django.http import JsonResponse

def whoiswho_json(request):

    data = {
        "type": "FeatureCollection",
        "features": [ w.json for w in WhoIsWho.objects.all() ]
    }

    return JsonResponse(data, safe=False)

def whoiswho_map(request):

    context = {}
    return render(request, 'whoiswho/index.html', context)
