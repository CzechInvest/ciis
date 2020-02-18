from django.db import models
from cigeo.models import Nuts3, Lau1
from django.utils.translation import ugettext_lazy as _


class Nuts3Stats(models.Model):

    class Meta:
        verbose_name = _("Kraj")
        verbose_name_plural = _("Kraje")

    year = models.IntegerField()

    nuts3 = models.ForeignKey(
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

    @property
    def json(self):
        nut3 = self.nuts3.json
        nut3["id"] = nut3["properties"]["code"]
        nut3["properties"]["population"] = self.population
        nut3["properties"]["work_power"] = self.work_power
        nut3["properties"]["unemployment"] = self.unemployment
        nut3["properties"]["unemployment_rate"] = self.unemployment_rate
        nut3["properties"]["unemployed_per_job"] = self.unemployed_per_job
        nut3["properties"]["medium_salary"] = self.medium_salary
        return nut3

    def __str__(self):
        return self.nuts3.name


class Lau1Stats(models.Model):

    class Meta:
        verbose_name = _("Okres")
        verbose_name_plural = _("Okresy")

    year = models.IntegerField()

    lau1 = models.ForeignKey(
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

    @property
    def json(self):
        lau1 = self.lau1.json
        lau1["id"] = lau1["properties"]["code"]
        lau1["properties"]["population"] = self.population
        lau1["properties"]["work_power"] = self.work_power
        lau1["properties"]["unemployment"] = self.unemployment
        lau1["properties"]["unemployment_rate"] = self.unemployment_rate
        lau1["properties"]["unemployed_per_job"] = self.unemployed_per_job
        return lau1

class Date(models.Model):
    date = models.DateField(unique=True)
    czk_euro = models.FloatField()
    czk_usd = models.FloatField()

    def __str__(self):
        return "{}".format(self.date)

class HumanResourcesLau1(models.Model):
    lau1 = models.ForeignKey(Lau1, on_delete=models.PROTECT)
    date = models.ForeignKey(Date, on_delete=models.PROTECT)
    inhabitans = models.IntegerField()
    productive_inhabitans = models.IntegerField()
    unemployed = models.IntegerField()
    vacancies = models.IntegerField()
    unemployment = models.FloatField()
    applications_per_vacancy = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.lau1, self.date)


class HumanResourcesNuts3(models.Model):
    nuts3 = models.ForeignKey(Nuts3, on_delete=models.PROTECT)
    date = models.ForeignKey(Date, on_delete=models.PROTECT)
    wages = models.IntegerField()
    inhabitans = models.IntegerField()
    productive_inhabitans = models.IntegerField()
    unemployed = models.IntegerField()
    vacancies = models.IntegerField()
    unemployment = models.FloatField()
    applications_per_vacancy = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.nuts3, self.date)
