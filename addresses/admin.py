from django.contrib import admin
from .models import Address

# Register your models here.
class AddressAdmin(admin.ModelAdmin):

    list_display = ("adm", "street", "number", "city", "zipcode",)

    search_fields = ("street", "city__name", "zipcode",)

admin.site.register(Address, AddressAdmin)
