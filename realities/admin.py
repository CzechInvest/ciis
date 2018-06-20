from django.contrib import admin
from django.urls import reverse
import nested_admin
import json
from .models import RealEstate
from .models import Attachment
from .models import Photo
from .models import Keyword
from .models import Electricity
from .models import DrinkingWater
from .models import NonPotableWater
from .models import Gas
from .models import WasteWater
from .models import Telecommunications
from .models import Area
from .models import AreaArea
from .models import AreaOwnership
from .models import Purpose
from .models import AreaArea
from .models import AreaPrice
from .models import Building
from .models import BuildingArea
from .models import BuildingDisposal
from .models import BuildingPrice
from .models import BuildingOwnership
from .models import Floor
from .models import SellingPrice
from .models import RentalPrice
from .models import Agent
from .models import Owner
from .models import Location

from cigeo.admin import NUTS3Filter
from cigeo.models import Lau1
from cigeo.models import Nuts3
from leaflet.admin import LeafletGeoAdmin
from cigeo.admin import NUTS3Filter
from cigeo.admin import ArealFieldAdmin
from cigeo.models import Road
from cigeo.forms import LocationForm

class LocationInline(LeafletGeoAdmin, nested_admin.NestedStackedInline):
    form = LocationForm
    model=Location
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    def __init__(self, *args, **kwargs):
        nested_admin.NestedStackedInline.__init__(self, parent_model=args[0], admin_site=args[1])
        #LeafletGeoAdmin.__init__(self, MyLocation, args[1])

class BuildingOwnershipInline(nested_admin.NestedStackedInline):
    extra = 0
    model=BuildingOwnership

class PurposeInline(nested_admin.NestedStackedInline):
    extra = 0
    model=Purpose

class AreaOwnershipInline(nested_admin.NestedStackedInline):
    extra = 0
    model=AreaOwnership

class SellingPriceInline(nested_admin.NestedStackedInline):
    extra = 0
    model=SellingPrice

class RentalPriceInline(nested_admin.NestedStackedInline):
    extra = 0
    model=RentalPrice

class AreaAreaInline(nested_admin.NestedStackedInline):
    extra = 0
    model=AreaArea

class DrinkingWaterInline(nested_admin.NestedStackedInline):
    extra = 0
    model=DrinkingWater

class ElectricityInline(nested_admin.NestedStackedInline):
    extra = 0
    model=Electricity

class NonPotableWaterInline(nested_admin.NestedStackedInline):
    extra = 0
    model=NonPotableWater

class GasInline(nested_admin.NestedStackedInline):
    extra = 0
    model=Gas

class WasteWaterInline(nested_admin.NestedStackedInline):
    extra = 0
    model=WasteWater

class TelecommunicationsInline(nested_admin.NestedStackedInline):
    extra = 0
    model=Telecommunications

class FloorInline(nested_admin.NestedStackedInline):
    extra = 0
    model=Floor

class BuildingInline(nested_admin.NestedStackedInline):
    extra = 0
    inlines = (BuildingOwnershipInline, FloorInline, )
    model=Building

class BuildingAreaInline(nested_admin.NestedStackedInline):
    extra = 0
    model=BuildingArea

class BuildingDisposalInline(nested_admin.NestedStackedInline):
    extra = 0
    model=BuildingDisposal

class BuildingPriceInline(nested_admin.NestedStackedInline):
    extra = 0
    model=BuildingDisposal


class PhotoInline(nested_admin.NestedStackedInline):
    extra = 0
    model=Photo

class AttachmentInline(nested_admin.NestedStackedInline):
    extra = 0
    model=Attachment

class AreaPriceAdmin(admin.ModelAdmin):
    pass


class AreaPriceInline(nested_admin.NestedStackedInline):
    model=AreaPrice
    extra = 0

    inlines = (SellingPriceInline, RentalPriceInline, )

class AreaAdmin(nested_admin.NestedModelAdmin):
    inlines = (AreaPriceInline, )
    extra = 0

class AreaInline(nested_admin.NestedStackedInline):
    extra = 0
    inlines = (AreaOwnershipInline, PurposeInline, AreaAreaInline,
            AreaPriceInline, BuildingInline)
    model=Area


class RealEstateAdmin(ArealFieldAdmin):
    search_fields = ("title", "realestate_type", "agent__first_name",
                     "agent__last_name", "location__address__city__name",
                     "owner__first_name", "owner__last_name")
    list_filter = (NUTS3Filter, )
    list_display = ("title", "realestate_type", "agent", "owner", "place",
                    "size")
    change_list_template = "admin/change_list-map.html"
    inlines = (LocationInline, PhotoInline, AttachmentInline,
               ElectricityInline, DrinkingWaterInline, NonPotableWaterInline,
               GasInline, WasteWaterInline, TelecommunicationsInline,
               AreaInline)

    def size(self, real_estate):
        if hasattr(real_estate, "area"):
            return real_estate.area.areaarea.total
        else:
            return None


    def place(self, obj):
        """Used in the ChangeList view as "Location" column name
        Display either City name or NUTS3 (Kraj) name
        """

        return self.get_place(obj)

class LocationAdmin(LeafletGeoAdmin):

    form = LocationForm
    raw_id_fields = ("address",)

    def get_form(self, request, obj=None, **kwargs):
        form = super(LocationAdmin, self).get_form(request, obj=obj, **kwargs)
        form.obj = obj
        return form


# Register your models here.
admin.site.register(RealEstate,RealEstateAdmin)
#admin.site.register(Photo)
#admin.site.register(Attachment)
#admin.site.register(Keyword)
#admin.site.register(Electricity)
#admin.site.register(DrinkingWater)
#admin.site.register(NonPotableWater)
#admin.site.register(Gas)
#admin.site.register(WasteWater)
#admin.site.register(Telecommunications)
#admin.site.register(Area, AreaAdmin)
#admin.site.register(AreaOwnership)
#admin.site.register(Purpose)
#admin.site.register(AreaArea)
#admin.site.register(AreaPrice, AreaPriceAdmin)
#admin.site.register(Building)
#admin.site.register(BuildingArea)
#admin.site.register(BuildingPrice)
#admin.site.register(BuildingDisposal)
#admin.site.register(Floor)
#admin.site.register(SellingPrice)
admin.site.register(Location, LocationAdmin)
admin.site.register(Agent)
admin.site.register(Owner)
