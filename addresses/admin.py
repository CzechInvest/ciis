from django.contrib import admin
from .models import Address
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin


class AddressAdmin(LeafletGeoAdmin):

    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    list_display = ("adm", "street", "number", "city", "zipcode",)

    search_fields = ("street", "orientation_number", "house_number",
                     "city__name", "zipcode",)

    def number(self, address):
        return address.number

    # def get_search_results(self, request, queryset, search_term):
    #    print(dir(queryset))


admin.site.register(Address, AddressAdmin)
