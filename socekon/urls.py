from django.urls import path

from . import views

urlpatterns = [
    path('nuts3/', views.MapViewNuts3.as_view(), name="socekon_nuts3_map"),
    path('nuts3/json', views.nuts3_json, name="socekon_nuts3_json"),
    path('nuts3/csv', views.nuts3_csv, name="socekon_nuts3_csv"),
    path('lau1/', views.MapViewLau1.as_view(), name="socekon_lau1_map"),
    path('lau1/json', views.lau1_json, name="socekon_lau1_json"),
    path('lau1/csv', views.lau1_csv, name="socekon_lau1_csv"),
]
