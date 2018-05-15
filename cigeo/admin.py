from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from leaflet.admin import LeafletGeoAdmin
from .models import Location
from .models import Lau1


class LocationAdmin(LeafletGeoAdmin):
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

class LAU1Admin(LeafletGeoAdmin):
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(Lau1, LAU1Admin)
