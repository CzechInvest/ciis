from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import IndustrialArealLocation
from ..models import IndustrialArealPhoto
from ..models import IndustrialArealAttachment
from ..models import IndustrialArealElectricity
from ..models import IndustrialArealDrinkWater
from ..models import IndustrialArealTechnologicalWater
from ..models import IndustrialArealGas
from ..models import IndustrialArealWasteWater
from ..models import IndustrialArealTelecommunication
from ..models import IndustrialArealGenericNote

from ..forms.path import LocationForm

from leaflet.admin import LeafletGeoAdmin
import nested_admin

from .generic import AdminImageWidget


class IndustrialArealGenericNoteInline(nested_admin.NestedStackedInline):
    model = IndustrialArealGenericNote
    extra = 0


class IndustrialArealTelecommunicationInline(nested_admin.NestedStackedInline):
    model = IndustrialArealTelecommunication
    extra = 0


class IndustrialArealWasteWaterInline(nested_admin.NestedStackedInline):
    model = IndustrialArealWasteWater
    extra = 0


class IndustrialArealElectricityInline(nested_admin.NestedStackedInline):
    model = IndustrialArealElectricity
    extra = 0


class IndustrialArealDrinkWaterInline(nested_admin.NestedStackedInline):
    model = IndustrialArealDrinkWater
    extra = 0


class IndustrialArealTechnologicalWaterInline(
  nested_admin.NestedStackedInline):
    model = IndustrialArealTechnologicalWater
    extra = 0


class IndustrialArealTechnologicalWater(nested_admin.NestedStackedInline):
    model = IndustrialArealTechnologicalWater
    extra = 0


class IndustrialArealPhotoInline(nested_admin.NestedStackedInline):
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    extra = 0
    model = IndustrialArealPhoto


class IndustrialArealAttachmentInline(nested_admin.NestedStackedInline):
    extra = 0
    model = IndustrialArealAttachment


class IndustrialArealGasInline(nested_admin.NestedStackedInline):
    extra = 0
    model = IndustrialArealGas


class IndustrialArealLocationInline(LeafletGeoAdmin,
                               nested_admin.NestedStackedInline):
    model = IndustrialArealLocation
    form = LocationForm
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    def __init__(self, *args, **kwargs):
        nested_admin.NestedStackedInline.__init__(
            self, parent_model=args[0], admin_site=args[1])
        # LeafletGeoAdmin.__init__(self, MyLocation, args[1])


class IndustrialArealAdmin(nested_admin.NestedModelAdmin):

    inlines = (
        IndustrialArealGenericNoteInline,
        IndustrialArealLocationInline,
        IndustrialArealPhotoInline,
        IndustrialArealAttachmentInline,
        IndustrialArealElectricityInline,
        IndustrialArealTelecommunicationInline,
        IndustrialArealDrinkWaterInline,
        IndustrialArealTechnologicalWaterInline,
        IndustrialArealGasInline,
        IndustrialArealWasteWaterInline,
    )

    readonly_fields = ('uuid',)
    fieldsets = (
        (
            _("Basic information"),
            {
                'fields': ('name', 'contact_person', 'owner', "donation",
                           "status", "uuid")
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
                    'previous_usage',
                    'hydrogeological_survey',
                    'water_level',
                    'ecological_stress',
                    'levels',
                    'height',
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
                    'access_road',
                    'railway_siding',
                )
            }
        )
    )
