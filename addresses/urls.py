from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddressView.as_view(), name="addresses")
]
