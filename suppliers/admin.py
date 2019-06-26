from django.contrib import admin
import nested_admin

# Register your models here.

from .models import Supplier
from cigeo.admin import ArealFieldAdmin
from cigeo.admin import NUTS3Filter
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin


class SupplierAdmin(ArealFieldAdmin, LeafletGeoAdmin):

    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    change_list_template = "admin/change_list-map.html"
    list_filter = (NUTS3Filter, )
    pass

    def size(self, obj):
        return None

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_add_another'] = False
        extra_context['show_delete'] = False
        extra_context['show_save'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['read_only'] = True
        return super(SupplierAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


admin.site.register(Supplier, SupplierAdmin)
