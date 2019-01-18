from django.db import models
from cigeo.models import Nuts3, Lau1
from django.utils.translation import ugettext_lazy as _


class Nuts3Stats(models.Model):

    class Meta:
        verbose_name = _("Kraj")
        verbose_name_plural = _("Kraje")

    nuts3 = models.OneToOneField(
        Nuts3, on_delete=models.CASCADE,
        #parent_link=True,
        verbose_name=_("Kraj"))

    population = models.IntegerField(
        verbose_name=_("Population"),
    )

    work_power = models.IntegerField(
        verbose_name=_("Work power"),
    )

    unemployment = models.IntegerField(
        verbose_name=_("Unemployment"),
    )

    unemployment_rate = models.FloatField(
        verbose_name=_("Unemployment rate"),
    )

    unemployed_per_job = models.FloatField(
        verbose_name=_("Medium salary"),
    )

    medium_salary = models.IntegerField(
        verbose_name=_("Medium salary"),
    )

    def __str__(self):
        return self.nuts3.name


class Lau1Stats(models.Model):

    class Meta:
        verbose_name = _("Okres")
        verbose_name_plural = _("Okresy")

    lau1 = models.OneToOneField(
        Lau1, on_delete=models.CASCADE,
        #parent_link=True,
        verbose_name=_("Okres")
    )

    population = models.IntegerField(
        verbose_name=_("Population"),
    )

    work_power = models.IntegerField(
        verbose_name=_("Work power"),
    )

    unemployment = models.IntegerField(
        verbose_name=_("Unemployment"),
    )

    unemployment_rate = models.FloatField(
        verbose_name=_("Unemployment rate"),
    )

    unemployed_per_job = models.FloatField(
        verbose_name=_("Medium salary"),
    )

    def __str__(self):
        return self.lau1.name

