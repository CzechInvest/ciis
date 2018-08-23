from django.db import models
from contacts.models import ContactPerson as EstateContactPerson
from contacts.models import Owner as EstateOwner
from django.utils.translation import ugettext_lazy as _

from .greenfield import *
from .developmentpark import *
from .industrialareal import *
from .office import *
from .scientificpark import *
from .brownfield import *


class ContactPerson(EstateContactPerson):
    pass


class Owner(EstateOwner):
    pass


class Estate(models.Model):

    class Meta:
        abstract = True

    CZK = 'czk'
    EUR = 'eur'

    AGRICULTURAL = "agro"
    SERVICES = "service"
    LIVING = "living"
    INDUSTRY = "industry"
    MINING = "mining"
    TRANSPORT = "transport"
    TRAVELING = "traveling"
    MILITARY = "military"

    A = "a"
    B = "b"
    C = "c"

    YES = 0
    NO = 1
    PRESUMED = 2

    DOES_NOT_EXIST = 0
    REPARE_NEEDED = 1
    GOOD_SHAPE = 2

    PUBLIC = 0
    IN_PROGRESS = 1
    TOBE_APPROVED = 2
    DEACTIVATED = 3
    PRIVATE = 4

    status_choices = (
        (PUBLIC, _("public")),
        (IN_PROGRESS, _("in progress")),
        (TOBE_APPROVED, _("to be approved")),
        (DEACTIVATED, _("deactivated")),
        (PRIVATE, _("private"))
    )

    status = models.IntegerField(
        help_text=_("Status"),
        default=IN_PROGRESS,
        choices=status_choices
    )

    donation = models.BooleanField()

    name = models.CharField(
        max_length=32,
        help_text=_("Name")
    )

    contact_person = models.ForeignKey(
        "ContactPerson",
        on_delete=models.PROTECT
    )

    owner = models.ForeignKey(
        "Owner",
        on_delete=models.PROTECT
    )

    category_choices = (
        (A, "A"),
        (B, "B"),
        (C, "C"),
    )

    category = models.CharField(
            max_length=1,
            choices=category_choices,
            help_text=_("Category"))

    spatial_plan = models.CharField(
            max_length=255,
            help_text=_("Spatial plan"))

    description = models.TextField(
            help_text=_("Description"),
            blank=True)

    parcel_numbers = models.CharField(
            max_length=255,
            help_text=_("Parcel numbers"),
            blank=True)

    total_area = models.IntegerField(
            help_text=_("Total area <code>[m<sup>2</sup>]</code>"))

    build_area = models.IntegerField(
            help_text=_("Build area <code>[m<sup>2</sup>]</code>"))

    free_area = models.IntegerField(
            help_text=_("Free area <code>[m<sup>2</sup>]</code>"))

    can_divide = models.NullBooleanField(
        default=True)

    smallest_divide_size = models.IntegerField(
        help_text=_("Smallest size of divided "
                    "unit <code>m<sup>2</sup>]</code>"),
        null=True,
        blank=True)

    available_since = models.DateField(
            blank=True,
            null=True,
            help_text=_("Available since"))

    currency_choices = (
        (CZK, _("CZK")),
        (EUR, _("EUR"))
    )

    currency = models.CharField(
            max_length=3,
            choices=currency_choices,
            default=CZK,
            help_text=_("Currency"))

    selling_price_maximal = models.IntegerField(
        help_text=_("Maximal selling price <code>[CZK/m<sup>2</sup>]</code>"))

    selling_price_minimal = models.IntegerField(
        help_text=_("Minimal price <code>[CZK/m<sup>2</sup>]</code>"))

    rental_price_minimal = models.IntegerField(
        help_text=_("Minimal rental price "
                    "<code>[CZK/m<sup>2</sup>/month]</code>"))

    rental_price_maximal = models.IntegerField(
        help_text=_("Maximal rental price "
                    "<code>[CZK/m<sup>2</sup>/month]</code>"))

    service_price = models.IntegerField(
        help_text=_("Service price <code>[CZK/month]</code>. "
                    "Security, reception desk, ..."))

    price_note = models.TextField(
        blank=True,
        help_text=_("Price note"))

    previous_usage_choices = (
        (SERVICES, _("Public services")),
        (MILITARY, _("Military")),
        (AGRICULTURAL, _("Agrucultural")),
        (INDUSTRY, _("Industry")),
        (MINING, _("Mining")),
        (LIVING, _("Living")),
        (TRANSPORT, _("Transporatation and logistics")),
        (TRAVELING, _("Traveling"))
    )

    previous_usage = models.CharField(
        max_length=16,
        choices=previous_usage_choices)

    hydrogeological_survey = models.NullBooleanField(
        blank=True,
    )

    water_level = models.IntegerField(
        null=True,
        blank=True
    )

    note = models.TextField(
        blank=True
    )

    ecological_stress_choices = (
        (YES, _("yes")),
        (NO, _("no")),
        (PRESUMED, _("presumed")),
    )

    ecological_stress = models.IntegerField(
        choices=ecological_stress_choices
    )

    levels = models.IntegerField(
        blank=True,
        null=True,
    )

    height = models.IntegerField(
        blank=True,
        null=True,
    )

    security = models.NullBooleanField(
        blank=True,
    )

    fire_protection = models.NullBooleanField(
        blank=True,
    )

    heating = models.NullBooleanField(
        blank=True,
    )

    air_condition = models.NullBooleanField(
        blank=True
    )

    crane = models.NullBooleanField(
        blank=True,
    )

    reception_desk = models.NullBooleanField(
        blank=True,
    )

    parking_place = models.IntegerField(
        blank=True,
        null=True
    )

    load_lift = models.NullBooleanField(
        blank=True,
    )

    personal_lift = models.NullBooleanField(
        blank=True,
    )

    canteen = models.NullBooleanField(
    )

    railway_siding = models.NullBooleanField(
    )

    other_equipment = models.TextField(blank=True)

    access_road_choices = (
        (DOES_NOT_EXIST, _("Does not exist")),
        (REPARE_NEEDED, _("Repair needed")),
        (GOOD_SHAPE, _("Good shape"))
    )

    access_road = models.IntegerField(
        choices=access_road_choices
    )


class GreenField(Estate):
    build_area = None
    service_price = None
    levels = None
    height = None
    security = None
    fire_protection = None
    heating = None
    air_condition = None
    crane = None
    reception_desk = None
    parking_place = None
    load_lift = None
    personal_lift = None
    canteen = None
    other_equipment = None

    agricultural_fund = models.BooleanField(
        help_text=_("Taken out of Agriculture fund"))

    af_removal_price = models.IntegerField(
        blank=True,
        null=True
    )


class DevelopmentPark(Estate):
    donation = models.NullBooleanField()
    ecological_stress = None


class IndustrialAreal(Estate):
    donation = models.NullBooleanField()


class Office(Estate):
    donation = models.NullBooleanField()
    total_area = None
    access_road = None
    railway_siding = None
    parcel_numbers = None


class ScientificPark(Estate):
    access_road = None
    railway_siding = None


class Brownfield(Estate):

    category = None

    description = models.TextField(
            help_text=_("Description"))

    parcel_numbers = models.CharField(
            max_length=255,
            help_text=_("Parcel numbers"))

    available_since = None

    service_price = None
    security = None
    fire_protection = None
    heating = None
    air_condition = None
    crane = None
    reception_desk = None
    parking_place = None
    load_lift = None
    personal_lift = None
    canteen = None
    other_equipment = None

