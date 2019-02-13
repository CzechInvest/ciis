from django.urls import path

from . import views

urlpatterns = [
    path('<int:address_id>', views.address),
    path('<int:address_id>/json', views.address_json),
    path('<slug:guery>', views.address_search),
    path('<slug:guery>/json', views.address_search_json),
]
