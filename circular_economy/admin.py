from django.contrib import admin
from .models import *


class MunicipalityAdmin(admin.ModelAdmin):

    raw_id_fields = ("address",)

class CompanyAdmin(admin.ModelAdmin):

    raw_id_fields = ("address",)

class PilotAdmin(admin.ModelAdmin):

    raw_id_fields = ("address",)


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Keyword)
admin.site.register(ContactPerson)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Pilot, PilotAdmin)
