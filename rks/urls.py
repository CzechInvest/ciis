from django.urls import path

from . import views

urlpatterns = [
    path('', views.MapRK.as_view(), name="rks_map"),
]
