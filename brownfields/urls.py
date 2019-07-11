from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /json/
    path('json/', views.bfsjson),
    path('json/<int:bf>/', views.bfjson),
]
