from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="cigeo_index"),
    path('lau1/', views.LAU1View.as_view(), name="cigeo_lau1_map"),
    path('nuts3/', views.NUTS3View.as_view(), name="cigeo_nuts3_map"),
]
