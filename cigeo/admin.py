from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from leaflet.admin import LeafletGeoAdmin
from .models import Location
#from leaflet.admin import LeafletGeoAdmin


class LocationAdmin(LeafletGeoAdmin):
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

# Register your models here.
admin.site.register(Location, LocationAdmin)
