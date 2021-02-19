from django.contrib import admin
from .models import Address
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from django.core.paginator import Paginator
from django.utils.functional import cached_property

class AddressPaginator(Paginator):
    """Addresses are not changing very often
    """

    @cached_property
    def count(self):
        try:
            return self.object_list.count()
        except (AttributeError, TypeError):
            return len(self.object_list)

class AddressAdmin(LeafletGeoAdmin):
    paginator = AddressPaginator

    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    list_display = ("adm", "street", "number", "city", "zipcode",)

    search_fields = ("street", "orientation_number", "house_number",
                     "city__name", "zipcode",)

    def number(self, address):
        return address.number

    def get_search_results(self, request, queryset, search_term):
        print(search_term)

        if "/" in search_term:
            nrs = list(filter(lambda x: "/" in x, search_term.split()))
            #house_number, orientation_number = [int(a) for a in nrs[0].split("/")]

        search_term = search_term.replace("/", " ")
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset, use_distinct
        pass


admin.site.register(Address, AddressAdmin)
