from django.urls import path

from . import views

urlpatterns = [
    path('', views.whoiswho_map),
    path('json', views.whoiswho_json, name="whoiswho_json"),
]
