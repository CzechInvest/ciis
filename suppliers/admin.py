from django.contrib import admin
import nested_admin

# Register your models here.

from .models import Supplier
from .models import ContactPerson
from .models import Certificate
from .models import Sector
from .models import Organisation
from .models import Location
from cigeo.admin import ArealFieldAdmin
from cigeo.admin import NUTS3Filter


class LocationAdminInline(nested_admin.NestedStackedInline):
    model = Location
    raw_id_fields = ("address",)
    extra = 1


class ContactPersonAdminInline(nested_admin.NestedStackedInline):
    model = ContactPerson


class OrganisationAdminInline(nested_admin.NestedStackedInline):
    model = Organisation
    inlines = (ContactPersonAdminInline, )
    raw_id_fields = ("address",)
    extra = 1


class SupplierAdmin(ArealFieldAdmin):
    change_list_template = "admin/change_list-map.html"
    inlines = (OrganisationAdminInline, LocationAdminInline, )
    list_filter = (NUTS3Filter, )
    pass

    def size(self, obj):
        return None


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Sector)
admin.site.register(Certificate)
