from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import ScientificParkLocation
from ..models import ScientificParkPhoto
from ..models import ScientificParkAttachment
from ..models import ScientificParkElectricity
from ..models import ScientificParkDrinkWater
from ..models import ScientificParkTechnologicalWater
from ..models import ScientificParkGas
from ..models import ScientificParkWasteWaterSevage
from ..models import ScientificParkWasteWaterRain
from ..models import ScientificParkWasteWaterIndustrial
from ..models import ScientificParkTelecommunication
from ..models import ScientificParkGenericNote

from ..forms import LocationForm

from leaflet.admin import LeafletGeoAdmin
import nested_admin

from .generic import AdminImageWidget


class ScientificParkGenericNoteInline(nested_admin.NestedStackedInline):
    model = ScientificParkGenericNote
    extra = 0


class ScientificParkTelecommunicationInline(nested_admin.NestedStackedInline):
    model = ScientificParkTelecommunication
    extra = 0


class ScientificParkWasteWaterSevageInline(nested_admin.NestedStackedInline):
    model = ScientificParkWasteWaterSevage
    extra = 0


class ScientificParkWasteWaterRainInline(nested_admin.NestedStackedInline):
    model = ScientificParkWasteWaterRain
    extra = 0


class ScientificParkWasteWaterIndustrialInline(nested_admin.NestedStackedInline):
    model = ScientificParkWasteWaterIndustrial
    extra = 0


class ScientificParkElectricityInline(nested_admin.NestedStackedInline):
    model = ScientificParkElectricity
    extra = 0


class ScientificParkDrinkWaterInline(nested_admin.NestedStackedInline):
    model = ScientificParkDrinkWater
    extra = 0


class ScientificParkTechnologicalWaterInline(nested_admin.NestedStackedInline):
    model = ScientificParkTechnologicalWater
    extra = 0


class ScientificParkTechnologicalWater(nested_admin.NestedStackedInline):
    model = ScientificParkTechnologicalWater
    extra = 0


class ScientificParkPhotoInline(nested_admin.NestedStackedInline):
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    extra = 0
    model = ScientificParkPhoto


class ScientificParkAttachmentInline(nested_admin.NestedStackedInline):
    extra = 0
    model = ScientificParkAttachment


class ScientificParkGasInline(nested_admin.NestedStackedInline):
    extra = 0
    model = ScientificParkGas


class ScientificParkLocationInline(LeafletGeoAdmin,
                               nested_admin.NestedStackedInline):
    model = ScientificParkLocation
    form = LocationForm
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    def __init__(self, *args, **kwargs):
        nested_admin.NestedStackedInline.__init__(
            self, parent_model=args[0], admin_site=args[1])
        # LeafletGeoAdmin.__init__(self, MyLocation, args[1])


class ScientificParkAdmin(nested_admin.NestedModelAdmin):

    inlines = (
        ScientificParkGenericNoteInline,
        ScientificParkLocationInline,
        ScientificParkPhotoInline,
        ScientificParkAttachmentInline,
        ScientificParkElectricityInline,
        ScientificParkTelecommunicationInline,
        ScientificParkDrinkWaterInline,
        ScientificParkTechnologicalWaterInline,
        ScientificParkGasInline,
        ScientificParkWasteWaterSevageInline,
        ScientificParkWasteWaterRainInline,
        ScientificParkWasteWaterIndustrialInline,
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
                    # 'parcel_numbers',
                    'total_area',
                    'free_area',
                    'build_area',
                    'can_divide',
                    'smallest_divide_size',
                    'available_since',
                    'currency',
                    'selling_price_minimal',
                    'selling_price_maximal',
                    'rental_price_minimal',
                    'rental_price_maximal',
                    'service_price',
                    'price_note',
                )
            }
        ),
        (
            _("Detailed information"),
            {
                'classes': ('collapse',),
                'fields': (
                    # 'agricultural_fund',
                    # 'af_removal_price',
                    # 'previous_usage',
                    # 'hydrogeological_survey',
                    # 'water_level',
                    # 'ecological_stress',
                    # 'levels',
                    # 'height',
                    'note',
                    'security',
                    'fire_protection',
                    'heating',
                    'air_condition',
                    'crane',
                    'reception_desk',
                    'parking_place',
                    'load_lift',
                    'personal_lift',
                    'canteen',
                    'other_equipment',
                    # 'access_road',
                    # 'railway_siding',
                )
            }
        )
    )
