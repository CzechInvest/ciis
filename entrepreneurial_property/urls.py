from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /json/
    path('', views.public_estates),
    path('new/', views.estate_new),
    path('<slug:uuid>/', views.estate_render),
    path('<slug:uuid>/edit', views.estate_edit),
]
