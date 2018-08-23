from django.db import models
from django.utils.translation import ugettext_lazy as _

from entrepreneurial_property.models import GreenFieldLocation
from entrepreneurial_property.models import GreenFieldPhoto
from entrepreneurial_property.models import GreenFieldAttachment
from entrepreneurial_property.models import GreenFieldElectricity
from entrepreneurial_property.models import GreenFieldDrinkWater
from entrepreneurial_property.models import GreenFieldTechnologicalWater
from entrepreneurial_property.models import GreenFieldGas
from entrepreneurial_property.models import GreenFieldWasteWaterSevage
from entrepreneurial_property.models import GreenFieldWasteWaterRain
from entrepreneurial_property.models import GreenFieldWasteWaterIndustrial
from entrepreneurial_property.models import GreenFieldTelecommunication
from entrepreneurial_property.models import GreenFieldGenericNote

from entrepreneurial_property.forms import LocationForm

from leaflet.admin import LeafletGeoAdmin
import nested_admin

from .generic import AdminImageWidget


class GreenFieldGenericNoteInline(nested_admin.NestedStackedInline):
    model = GreenFieldGenericNote
    extra = 0


class GreenFieldTelecommunicationInline(nested_admin.NestedStackedInline):
    model = GreenFieldTelecommunication
    extra = 0


class GreenFieldWasteWaterSevageInline(nested_admin.NestedStackedInline):
    model = GreenFieldWasteWaterSevage
    extra = 0


class GreenFieldWasteWaterRainInline(nested_admin.NestedStackedInline):
    model = GreenFieldWasteWaterRain
    extra = 0


class GreenFieldWasteWaterIndustrialInline(nested_admin.NestedStackedInline):
    model = GreenFieldWasteWaterIndustrial
    extra = 0


class GreenFieldElectricityInline(nested_admin.NestedStackedInline):
    model = GreenFieldElectricity
    extra = 0


class GreenFieldDrinkWaterInline(nested_admin.NestedStackedInline):
    model = GreenFieldDrinkWater
    extra = 0


class GreenFieldTechnologicalWaterInline(nested_admin.NestedStackedInline):
    model = GreenFieldTechnologicalWater
    extra = 0


class GreenFieldTechnologicalWater(nested_admin.NestedStackedInline):
    model = GreenFieldTechnologicalWater
    extra = 0


class GreenFieldPhotoInline(nested_admin.NestedStackedInline):
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    extra = 0
    model = GreenFieldPhoto


class GreenFieldAttachmentInline(nested_admin.NestedStackedInline):
    extra = 0
    model = GreenFieldAttachment


class GreenFieldGasInline(nested_admin.NestedStackedInline):
    extra = 0
    model = GreenFieldGas


class GreenFieldLocationInline(LeafletGeoAdmin,
                               nested_admin.NestedStackedInline):
    model = GreenFieldLocation
    form = LocationForm
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    def __init__(self, *args, **kwargs):
        nested_admin.NestedStackedInline.__init__(
            self, parent_model=args[0], admin_site=args[1])
        # LeafletGeoAdmin.__init__(self, MyLocation, args[1])


class GreenFieldAdmin(nested_admin.NestedModelAdmin):

    inlines = (
        GreenFieldGenericNoteInline,
        GreenFieldLocationInline,
        GreenFieldPhotoInline,
        GreenFieldAttachmentInline,
        GreenFieldElectricityInline,
        GreenFieldTelecommunicationInline,
        GreenFieldDrinkWaterInline,
        GreenFieldTechnologicalWaterInline,
        GreenFieldGasInline,
        GreenFieldWasteWaterSevageInline,
        GreenFieldWasteWaterRainInline,
        GreenFieldWasteWaterIndustrialInline,
    )

    # readonly_fields = ('available_since',)
    fieldsets = (
        (
            _("Basic information"),
            {
                'fields': ('name', 'contact_person', 'owner', "donation",
                           "status")
            }
        ),
        (
            _("Characteristics"),
            {
                'fields': (
                    'category',
                    'spatial_plan',
                    'description',
                    'parcel_numbers',
                    'total_area',
                    'free_area',
                    'can_divide',
                    'smallest_divide_size',
                    'available_since',
                    'currency',
                    'selling_price_minimal',
                    'selling_price_maximal',
                    'rental_price_minimal',
                    'rental_price_maximal',
                    # 'service_price',
                    'price_note',
                )
            }
        ),
        (
            _("Detailed information"),
            {
                'classes': ('collapse',),
                'fields': (
                    'agricultural_fund',
                    'af_removal_price',
                    'previous_usage',
                    'hydrogeological_survey',
                    'water_level',
                    'ecological_stress',
                    # 'levels',
                    # 'height',
                    'note',
                    # 'security',
                    # 'fire_protection',
                    # 'heating',
                    # 'air_condition',
                    # 'crane',
                    # 'reception_desk',
                    # 'parking_place',
                    # 'load_lift',
                    # 'personal_lift',
                    # 'canteen',
                    # 'other_equipment',
                    'access_road',
                    'railway_siding',
                )
            }
        )
    )

    search_fields = ("name", "donation", "contact_person__last_name", "owner__name", "category",
                     "spatial_plan", "total_area")

    list_display = ("name", "donation", "contact_person", "owner", "category",
                    "spatial_plan", "total_area")
