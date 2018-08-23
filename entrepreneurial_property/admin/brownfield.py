from django.db import models
from django.utils.translation import ugettext_lazy as _

from entrepreneurial_property.models import BrownfieldLocation
from entrepreneurial_property.models import BrownfieldPhoto
from entrepreneurial_property.models import BrownfieldAttachment
from entrepreneurial_property.models import BrownfieldElectricity
from entrepreneurial_property.models import BrownfieldDrinkWater
from entrepreneurial_property.models import BrownfieldTechnologicalWater
from entrepreneurial_property.models import BrownfieldGas
from entrepreneurial_property.models import BrownfieldWasteWaterSevage
from entrepreneurial_property.models import BrownfieldWasteWaterRain
from entrepreneurial_property.models import BrownfieldWasteWaterIndustrial
from entrepreneurial_property.models import BrownfieldTelecommunication
from entrepreneurial_property.models import BrownfieldGenericNote

from entrepreneurial_property.forms import LocationForm

from leaflet.admin import LeafletGeoAdmin
import nested_admin

from .generic import AdminImageWidget


class BrownfieldGenericNoteInline(nested_admin.NestedStackedInline):
    model = BrownfieldGenericNote
    extra = 0


class BrownfieldTelecommunicationInline(nested_admin.NestedStackedInline):
    model = BrownfieldTelecommunication
    extra = 0


class BrownfieldWasteWaterSevageInline(nested_admin.NestedStackedInline):
    model = BrownfieldWasteWaterSevage
    extra = 0


class BrownfieldWasteWaterRainInline(nested_admin.NestedStackedInline):
    model = BrownfieldWasteWaterRain
    extra = 0


class BrownfieldWasteWaterIndustrialInline(nested_admin.NestedStackedInline):
    model = BrownfieldWasteWaterIndustrial
    extra = 0


class BrownfieldElectricityInline(nested_admin.NestedStackedInline):
    model = BrownfieldElectricity
    extra = 0


class BrownfieldDrinkWaterInline(nested_admin.NestedStackedInline):
    model = BrownfieldDrinkWater
    extra = 0


class BrownfieldTechnologicalWaterInline(nested_admin.NestedStackedInline):
    model = BrownfieldTechnologicalWater
    extra = 0


class BrownfieldTechnologicalWater(nested_admin.NestedStackedInline):
    model = BrownfieldTechnologicalWater
    extra = 0


class BrownfieldPhotoInline(nested_admin.NestedStackedInline):
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    extra = 0
    model = BrownfieldPhoto


class BrownfieldAttachmentInline(nested_admin.NestedStackedInline):
    extra = 0
    model = BrownfieldAttachment


class BrownfieldGasInline(nested_admin.NestedStackedInline):
    extra = 0
    model = BrownfieldGas


class BrownfieldLocationInline(LeafletGeoAdmin,
                               nested_admin.NestedStackedInline):
    model = BrownfieldLocation
    form = LocationForm
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    def __init__(self, *args, **kwargs):
        nested_admin.NestedStackedInline.__init__(
            self, parent_model=args[0], admin_site=args[1])
        # LeafletGeoAdmin.__init__(self, MyLocation, args[1])


class BrownfieldAdmin(nested_admin.NestedModelAdmin):

    inlines = (
        BrownfieldGenericNoteInline,
        BrownfieldLocationInline,
        BrownfieldPhotoInline,
        BrownfieldAttachmentInline,
        BrownfieldElectricityInline,
        BrownfieldTelecommunicationInline,
        BrownfieldDrinkWaterInline,
        BrownfieldTechnologicalWaterInline,
        BrownfieldGasInline,
        BrownfieldWasteWaterSevageInline,
        BrownfieldWasteWaterRainInline,
        BrownfieldWasteWaterIndustrialInline,
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
                    # 'category',
                    'spatial_plan',
                    'description',
                    'parcel_numbers',
                    'total_area',
                    'free_area',
                    'can_divide',
                    'smallest_divide_size',
                    # 'available_since',
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
                    'previous_usage',
                    'hydrogeological_survey',
                    'water_level',
                    'ecological_stress',
                    'levels',
                    'height',
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
