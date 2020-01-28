from django.contrib import admin
from .models import VtpType, Service, Vtp
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from cigeo.admin import ArealFieldAdmin


class VtpAdmin(ArealFieldAdmin, LeafletGeoAdmin):

    list_display = (
            "name", "my_type", "my_services", "url")
    change_list_template = "admin/change_list-map.html"
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    def my_type(self, obj):
        return ", ".join([str(i) for i in obj.type.all()])

    def my_services(self, obj):
        return ", ".join([str(i) for i in obj.services.all()])

# Register your models here.
admin.site.register(VtpType)
admin.site.register(Service)
admin.site.register(Vtp, VtpAdmin)
