from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="socekon_index"),
    path('nuts3/', views.MapViewNuts3.as_view(), name="socekon_nuts3_map"),
    path('lau1/', views.MapViewLau1.as_view(), name="socekon_lau1_map"),
]
