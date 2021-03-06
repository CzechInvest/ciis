from django.contrib import admin
import nested_admin
import json
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib.gis import geos

from cigeo.models import Lau1
from cigeo.admin import NUTS3Filter
from cigeo.admin import ArealFieldAdmin
from leaflet.admin import LeafletGeoAdmin

from django.contrib.admin.widgets import AdminFileWidget
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

#from .models import Location
from .models import Brownfield
#from .models import Photo
#from .models import Attachment
#from .models import Areal
#from .models import EcologicalLimit
#from .models import ResearchFieldWork
#from .models import CulturalProtection
#from .models import GeologicalLimit
#from .models import NatureConversation
#from .models import WaterConservation
#from .models import RoadBuffer
#from .models import NetworksBuffer
#from .models import AgriculturalProtection
#from .models import OtherLimits
#from .models import EIA
#from .models import Ownership
#from .models import Electricity
#from .models import DrinkingWater
#from .models import NonPotableWater
#from .models import Gas
#from .models import WasteWater
#from .models import Telecommunications
#from .models import Road
#from .models import RailRoad
#from .models import Area
#from .models import Keeper


class BrownfieldAdmin(ArealFieldAdmin, LeafletGeoAdmin):

    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    list_display = [
        "name", "status", "address", "total_area", "built_up_area",
        "selling_price"
    ]

    change_list_template = "admin/change_list-map.html"
    list_filter = (NUTS3Filter, )
    pass

    def size(self, obj):
        return None

    def selling_price(self, obj):
        return "{} - {}".format(obj.selling_price_from, obj.selling_price_to)

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_add_another'] = False
        extra_context['show_delete'] = False
        extra_context['show_save'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['read_only'] = True
        return super(BrownfieldAdmin, self).changeform_view(request, object_id, extra_context=extra_context)



#class KeeperInline(nested_admin.NestedStackedInline):
#    model = Keeper
#    extra = 0
#
#
#class EcologicalLimitInline(nested_admin.NestedStackedInline):
#    model = EcologicalLimit
#    extra = 0
#
#
#class ResearchFieldWorkInline(nested_admin.NestedStackedInline):
#    model = ResearchFieldWork
#    extra = 0
#
#
#class CulturalProtectionInline(nested_admin.NestedStackedInline):
#    model = CulturalProtection
#    extra = 0
#
#
#class GeologicalLimitInline(nested_admin.NestedStackedInline):
#    model = GeologicalLimit
#    extra = 0
#
#
#class NatureConversationInline(nested_admin.NestedStackedInline):
#    model = NatureConversation
#    extra = 0
#
#
#class WaterConservationInline(nested_admin.NestedStackedInline):
#    model = WaterConservation
#    extra = 0
#
#
#class RoadBufferInline(nested_admin.NestedStackedInline):
#    model = RoadBuffer
#    extra = 0
#
#
#class NetworksBufferInline(nested_admin.NestedStackedInline):
#    model = NetworksBuffer
#    extra = 0
#
#
#class AgriculturalProtectionInline(nested_admin.NestedStackedInline):
#    model = AgriculturalProtection
#    extra = 0
#
#
#class OtherLimitsInline(nested_admin.NestedStackedInline):
#    model = OtherLimits
#    extra = 0
#
#
#class EIAInline(nested_admin.NestedStackedInline):
#    model = EIA
#    extra = 0
#
#
#class OwnershipInline(nested_admin.NestedStackedInline):
#    model = Ownership
#    extra = 0
#
#
#class ElectricityInline(nested_admin.NestedStackedInline):
#    model = Electricity
#    extra = 0
#
#
#class DrinkingWaterInline(nested_admin.NestedStackedInline):
#    model = DrinkingWater
#    extra = 0
#
#
#class NonPotableWaterInline(nested_admin.NestedStackedInline):
#    model = NonPotableWater
#    extra = 0
#
#
#class GasInline(nested_admin.NestedStackedInline):
#    model = Gas
#    extra = 0
#
#
#class WasteWaterInline(nested_admin.NestedStackedInline):
#    model = WasteWater
#    extra = 0
#
#
#class TelecommunicationsInline(nested_admin.NestedStackedInline):
#    model = Telecommunications
#    extra = 0
#
#
#class RoadInline(nested_admin.NestedStackedInline):
#    model = Road
#    extra = 0
#
#
#class RailRoadInline(nested_admin.NestedStackedInline):
#    model = RailRoad
#    extra = 0
#
#
#class AreaInline(nested_admin.NestedStackedInline):
#    model = Area
#    extra = 0
#
#
#class AdminImageWidget(AdminFileWidget):
#    def render(self, name, value, attrs=None):
#        output = []
#        if value and getattr(value, "url", None):
#            image_url = value.url
#            file_name = str(value)
#            output.append(
#                u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s ' %
#                (image_url, image_url, file_name, _('')))
#            output.append(
#                super(
#                    AdminFileWidget,
#                    self).render(
#                    name,
#                    value,
#                    attrs))
#        return mark_safe(u''.join(output))
#
#
#class PhotoInline(nested_admin.NestedStackedInline):
#    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
#    extra = 0
#    model = Photo
#
#
#class AttachmentInline(nested_admin.NestedStackedInline):
#    extra = 0
#    model = Attachment
#
#
#class LocationInline(LeafletGeoAdmin, nested_admin.NestedStackedInline):
#    model = Location
#    form = LocationForm
#    raw_id_fields = ("address",)
#    default_zoom = 7
#    default_lon = 1730000
#    default_lat = 6430000
#
#    def __init__(self, *args, **kwargs):
#        nested_admin.NestedStackedInline.__init__(
#            self, parent_model=args[0], admin_site=args[1])
#        # LeafletGeoAdmin.__init__(self, MyLocation, args[1])
#
#
#class ArealInline(nested_admin.NestedStackedInline):
#    model = Areal
#    inlines = (
#        KeeperInline,
#        EcologicalLimitInline,
#        ResearchFieldWorkInline,
#        CulturalProtectionInline,
#        GeologicalLimitInline,
#        NatureConversationInline,
#        WaterConservationInline,
#        RoadBufferInline,
#        NetworksBufferInline,
#        AgriculturalProtectionInline,
#        OtherLimitsInline,
#        EIAInline,
#        OwnershipInline,
#        ElectricityInline,
#        DrinkingWaterInline,
#        NonPotableWaterInline,
#        GasInline,
#        WasteWaterInline,
#        TelecommunicationsInline,
#        RoadInline,
#        RailRoadInline,
#        AreaInline,
#    )
#
#
#class BrownfieldAdmin(ArealFieldAdmin):
#    search_fields = (
#        "title",
#        "status",
#        "local_type",
#        "location__address__city__name",
#        #"keeper__first_name",
#        #"keeper__last_name")
#    )
#    list_filter = (NUTS3Filter, )
#    change_list_template = "admin/change_list-map.html"
#    list_display = ("title", "status", "local_type", "place", "size")
#    inlines = (LocationInline, PhotoInline, AttachmentInline,
#               ArealInline,)
#
#    # change_list_template
#
#    def size(self, brownfield):
#        if hasattr(brownfield, "areal") and\
#                hasattr(brownfield.areal, "area"):
#            return brownfield.areal.area.total
#        else:
#            return None
#
#    def place(self, obj):
#        """Used in the ChangeList view as "Location" column name
#        Display either City name or NUTS3 (Kraj) name
#        """
#
#        return self.get_place(obj)
#
#
#class LocationAdmin(LeafletGeoAdmin):
#
#    form = LocationForm
#    raw_id_fields = ("address",)
#
#    def get_form(self, request, obj=None, **kwargs):
#        form = super(LocationAdmin, self).get_form(request, obj=obj, **kwargs)
#        form.obj = obj
#        return form


# Register your models here.

admin.site.register(Brownfield, BrownfieldAdmin)
#admin.site.register(Areal)
#admin.site.register(Photo)
#admin.site.register(Location, LocationAdmin)
