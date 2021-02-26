from django.contrib import admin
from dynamic_raw_id.admin import DynamicRawIDMixin

from .models import RK

# Register your models here.

class RKAdmin(DynamicRawIDMixin, admin.ModelAdmin):


    dynamic_raw_id_fields = ("address")
    search_fields = ("name", "director")
    list_display = ("name", "director", "address", "email", "phone")

admin.site.register(RK, RKAdmin)
