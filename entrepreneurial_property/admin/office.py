from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import OfficeLocation
from ..models import OfficePhoto
from ..models import OfficeAttachment
from ..models import OfficeElectricity
from ..models import OfficeDrinkWater
from ..models import OfficeTechnologicalWater
from ..models import OfficeGas
from ..models import OfficeWasteWater
from ..models import OfficeTelecommunication
from ..models import OfficeGenericNote

from ..forms.path import LocationForm

from leaflet.admin import LeafletGeoAdmin
import nested_admin

from .generic import AdminImageWidget


class OfficeGenericNoteInline(nested_admin.NestedStackedInline):
    model = OfficeGenericNote
    extra = 0


class OfficeTelecommunicationInline(nested_admin.NestedStackedInline):
    model = OfficeTelecommunication
    extra = 0


class OfficeWasteWaterInline(nested_admin.NestedStackedInline):
    model = OfficeWasteWater
    extra = 0


class OfficeElectricityInline(nested_admin.NestedStackedInline):
    model = OfficeElectricity
    extra = 0


class OfficeDrinkWaterInline(nested_admin.NestedStackedInline):
    model = OfficeDrinkWater
    extra = 0


class OfficeTechnologicalWaterInline(nested_admin.NestedStackedInline):
    model = OfficeTechnologicalWater
    extra = 0


class OfficeTechnologicalWater(nested_admin.NestedStackedInline):
    model = OfficeTechnologicalWater
    extra = 0


class OfficePhotoInline(nested_admin.NestedStackedInline):
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    extra = 0
    model = OfficePhoto


class OfficeAttachmentInline(nested_admin.NestedStackedInline):
    extra = 0
    model = OfficeAttachment


class OfficeGasInline(nested_admin.NestedStackedInline):
    extra = 0
    model = OfficeGas


class OfficeLocationInline(LeafletGeoAdmin,
                               nested_admin.NestedStackedInline):
    model = OfficeLocation
    form = LocationForm
    raw_id_fields = ("address",)
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    def __init__(self, *args, **kwargs):
        nested_admin.NestedStackedInline.__init__(
            self, parent_model=args[0], admin_site=args[1])
        # LeafletGeoAdmin.__init__(self, MyLocation, args[1])


class OfficeAdmin(nested_admin.NestedModelAdmin):

    inlines = (
        OfficeGenericNoteInline,
        OfficeLocationInline,
        OfficePhotoInline,
        OfficeAttachmentInline,
        OfficeElectricityInline,
        OfficeTelecommunicationInline,
        OfficeDrinkWaterInline,
        OfficeTechnologicalWaterInline,
        OfficeGasInline,
        OfficeWasteWaterInline,
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
                    # 'parcel_numbers',
                    # 'total_area',
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
