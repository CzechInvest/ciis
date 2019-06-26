from django.urls import path

from . import views

urlpatterns = [
    path('nuts3/json', views.nuts3_json),
    path('lau1/json', views.lau1_json),
]
