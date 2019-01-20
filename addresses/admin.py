from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):

    list_display = ("adm", "street", "number", "city", "zipcode",)

    search_fields = ("street", "orientation_number", "house_number",
                     "city__name", "zipcode",)

    def number(self, address):
        return address.number

    # def get_search_results(self, request, queryset, search_term):
    #    print(dir(queryset))


admin.site.register(Address, AddressAdmin)
