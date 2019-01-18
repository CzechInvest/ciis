from django.contrib import admin
from .models import WhoIsWho
from .models import Institution
from .models import Keyword
from .models import Sector
from .models import Location
from .models import WhoIsWho
from .models import Specialization
from .models import ContactPerson

from leaflet.admin import LeafletGeoAdmin

import nested_admin


class LocationInline(LeafletGeoAdmin, nested_admin.NestedStackedInline):
    model = Location
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    def __init__(self, *args, **kwargs):
        nested_admin.NestedStackedInline.__init__(
            self, parent_model=args[0], admin_site=args[1])
        # LeafletGeoAdmin.__init__(self, MyLocation, args[1])


class WhoIsWhoInline(nested_admin.NestedStackedInline):
    model = WhoIsWho


class ContactPersonInline(nested_admin.NestedStackedInline):
    model = ContactPerson


class SpecializationInline(nested_admin.NestedStackedInline):
    model = Specialization
    inlines = ( ContactPersonInline, )

class InstitutionAdmin(nested_admin.NestedModelAdmin):
    model = Institution
    inlines = (
        LocationInline,
        WhoIsWhoInline,
        SpecializationInline
    )


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Keyword)
admin.site.register(Sector)
