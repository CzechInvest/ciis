from django.shortcuts import render
from .models import WhoIsWho
from django.http import JsonResponse

def whoiswho_json(request):

    data = [
        w.json for w in WhoIsWho.objects.all()
    ]

    return JsonResponse(data)

