from django.db import models
from django.utils.translation import ugettext_lazy as _


class Medium(models.Model):

    class Meta:
        abstract = True

    distance = models.IntegerField(
        default=0,
        verbose_name=_("Distnace"),
        help_text=_("Dinstance to object <code>[m]</code>")
    )

    note = models.TextField(
        blank=True,
        verbose_name=_("Note"),
        help_text=_("Note")
    )


class Water(Medium):

    class Meta:
        abstract = True

    diameter = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("Diameter"),
        help_text=_("<code>[mm]</code>")
    )
    capacity = models.IntegerField(
            verbose_name=_("Capacity"),
            blank=True,
            help_text=_("Capacity <code>[m<sup>3</sup>/d]</code>"))

    well = models.BooleanField(
            blank=True,
            verbose_name=_("Well")
    )

    well_capacity = models.IntegerField(
        blank=True,
        null=True,
        help_text=_("Well capacity <code>[m<sup>3</sup>/d]</code>")
    )


class Electricity(Medium):

    class Meta:
        abstract = True

    current = models.IntegerField(
            blank=True,
            verbose_name=_("Napětí"),
            help_text=_("Napětí <code>[kV]</code>"))

    capacity = models.IntegerField(
            verbose_name=_("Kapacita"),
            help_text=_("Kapacita <code>[MW]</code>"))


class WasteWater(Medium):

    class Meta:
        verbose_name = _("Odpadní voda")
        verbose_name_plural = _("Odpadní vody")
        abstract = True

    type_choices = (
        (0, _("Sevage")),
        (1, _("Rain")),
        (2, _("Industry"))
    )

    cleaning_type = models.CharField(max_length=10,
                                     verbose_name=_("Typ čistírny"),
                                     choices=type_choices)

    diameter = models.IntegerField(
            verbose_name=_("Průměr"),
            blank=True,
            help_text="Velikost přípojky <code>[mm]</code>")

    capacity = models.IntegerField(
            blank=True,
            verbose_name=_("Kapacita přípojky"),
            help_text="Kapacita přípojky <code>[m<sup>3</sup>/d]</code>")

    sevage_plant_name = models.TextField(
            blank=True,
            help_text="Name and address")

    technology_choices = ()

    sevage_plant_technology = models.CharField(
        blank=True,
        max_length=10,
        choices=technology_choices,
    )

    absorbtion = models.CharField(
        blank=True,
        max_length=64,
        help_text=_("River name, where the water will be absorbed")
    )


class Telecommunication(Medium):

    class Meta:
        abstract = True

    OPTIC = "optic"
    METALIC = "metalic"
    WIFI = "wifi"
    CELLULAR = "cell"

    technology_choices = (
        (OPTIC, _("Optic")),
        (METALIC, _("Metalic")),
        (WIFI, _("WIFI")),
        (CELLULAR, _("Cellular"))
    )

    technology = models.CharField(
        max_length=10,
        blank=True,
        choices=technology_choices
    )


class Gas(Medium):

    class Meta:
        abstract = True

    diameter = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("Diameter"),
        help_text=_("<code>[mm]</code>")
    )

    pressure = models.IntegerField(
            blank=True,
            verbose_name=_("Pressure"),
            help_text=_("Pressure <code>[kPa]</code>"))

    capacity = models.IntegerField(
            blank=True,
            verbose_name=_("Capacity"),
            help_text="Capacity <code>[m<sup>3</sup>/d]</code>")
