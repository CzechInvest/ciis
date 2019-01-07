from django.contrib import admin
from .models import Address

# Register your models here.
class AddressAdmin(admin.ModelAdmin):

    list_display = ("adm", "street", "number", "city", "zipcode",)

    search_fields = ("street", "house_number", "orientation_number", "city__name", "zipcode",)

    def number(self, address):
        return "{}/{}".format(address.house_number, address.orientation_number)

    def get_search_results(self, request, queryset, search_term):
        print(dir(queryset))

admin.site.register(Address, AddressAdmin)
