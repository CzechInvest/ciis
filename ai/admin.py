from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from cigeo.admin import ArealFieldAdmin
from .models import *

class AiAdmin(ArealFieldAdmin, LeafletGeoAdmin):

    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

admin.site.register(Form)
admin.site.register(Ai, AiAdmin)
