from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import DevelopmentParkLocation
from ..models import DevelopmentParkPhoto
from ..models import DevelopmentParkAttachment
from ..models import DevelopmentParkElectricity
from ..models import DevelopmentParkDrinkWater
from ..models import DevelopmentParkTechnologicalWater
from ..models import DevelopmentParkGas
from ..models import DevelopmentParkWasteWater
from ..models import DevelopmentParkTelecommunication
from ..models import DevelopmentParkGenericNote

from ..forms.path import LocationForm

from leaflet.admin import LeafletGeoAdmin
import nested_admin

from .generic import AdminImageWidget


class DevelopmentParkGenericNoteInline(nested_admin.NestedStackedInline):
    model = DevelopmentParkGenericNote
    extra = 0


class DevelopmentParkTelecommunicationInline(nested_admin.NestedStackedInline):
    model = DevelopmentParkTelecommunication
    extra = 0


class DevelopmentParkWasteWaterInline(nested_admin.NestedStackedInline):
    model = DevelopmentParkWasteWater
    extra = 0


class DevelopmentParkElectricityInline(nested_admin.NestedStackedInline):
    model = DevelopmentParkElectricity
    extra = 0


class DevelopmentParkDrinkWaterInline(nested_admin.NestedStackedInline):
    model = DevelopmentParkDrinkWater
    extra = 0


class DevelopmentParkTechnologicalWaterInline(
  nested_admin.NestedStackedInline):

    model = DevelopmentParkTechnologicalWater
    extra = 0


class DevelopmentParkTechnologicalWater(nested_admin.NestedStackedInline):
    model = DevelopmentParkTechnologicalWater
    extra = 0


class DevelopmentParkPhotoInline(nested_admin.NestedStackedInline):
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    extra = 0
    model = DevelopmentParkPhoto


class DevelopmentParkAttachmentInline(nested_admin.NestedStackedInline):
    extra = 0
    model = DevelopmentParkAttachment


class DevelopmentParkGasInline(nested_admin.NestedStackedInline):
    extra = 0
    model = DevelopmentParkGas


class DevelopmentParkLocationInline(LeafletGeoAdmin,
                               nested_admin.NestedStackedInline):
    model = DevelopmentParkLocation
    form = LocationForm
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    def __init__(self, *args, **kwargs):
        nested_admin.NestedStackedInline.__init__(
            self, parent_model=args[0], admin_site=args[1])
        # LeafletGeoAdmin.__init__(self, MyLocation, args[1])


class DevelopmentParkAdmin(nested_admin.NestedModelAdmin):

    inlines = (
        DevelopmentParkGenericNoteInline,
        DevelopmentParkLocationInline,
        DevelopmentParkPhotoInline,
        DevelopmentParkAttachmentInline,
        DevelopmentParkElectricityInline,
        DevelopmentParkTelecommunicationInline,
        DevelopmentParkDrinkWaterInline,
        DevelopmentParkTechnologicalWaterInline,
        DevelopmentParkGasInline,
        DevelopmentParkWasteWaterInline,
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
                    # 'ecological_stress',
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
