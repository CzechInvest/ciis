from django.contrib.gis.db import models
from addresses.models import Address
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import json


class Nuts3(models.Model):

    class Meta:
        verbose_name = _("Kraj")
        verbose_name_plural = _("Kraje")

    code = models.IntegerField(
            verbose_name=_("Kód")
    )

    name = models.CharField(
            verbose_name=_("Název"),
            max_length=256
    )

    geometry = models.MultiPolygonField(
            verbose_name=_("Hranice"),
            srid=4326)

    def __str__(self):
        return self.name

    @property
    def json(self):
        data = {
            "geometry": json.loads(self.geometry.json)
        }
        data["properties"] = {
            "name": self.name,
            "code": self.code
        }
        data["type"] = "Feature"

        return data


class Lau1(models.Model):
    # okresy

    class Meta:
        verbose_name = _("Okres")
        verbose_name_plural = _("Okresy")

    code = models.IntegerField(
            verbose_name=_("Kód")
    )

    name = models.CharField(
            verbose_name=_("Název"),
            max_length=256
    )

    geometry = models.MultiPolygonField(
            verbose_name=_("Hranice"),
            srid=4326)

    def __str__(self):
        return self.name

    @property
    def json(self):
        data = {
            "geometry": json.loads(self.geometry.json)
        }
        data["properties"] = {
            "name": self.name,
            "code": self.code
        }
        data["type"] = "Feature"

        return data


class Location(models.Model):

    class Meta:
        verbose_name = _("Umístění")
        verbose_name_plural = _("Umístění")
        abstract = True

    address = models.ForeignKey(
        Address,
        null=True,
        blank=True,
        related_name="+",
        verbose_name=_("Adresa"),
        on_delete=models.SET_NULL
    )

    geometry = models.GeometryCollectionField(
            verbose_name=_("Geometrie"),
            help_text=_("Geometrie"),
            null=True,
            blank=True,
            srid=4326)

    def __str__(self):
        if self.address:
            if self.address.house_number and self.address.orientation_number:
                hr = "{}/{}".format(self.address.house_number,
                                    self.address.orientation_number)
            elif self.address.house_number:
                hr = self.address.house_number
            elif self.address.orientation_number:
                hr = self.address.orientation_number
            else:
                hr = ""

            return "{} {}, {}".format(self.address.street,
                                      hr, self.address.city)
        else:
            if self.geometry:
                lau1s = ", ".join([l.name for l in Lau1.objects.filter(
                               geometry__intersects=self.geometry)])
                return lau1s
            else:
                return ""

    @property
    def json(self):
        data = {
            "geometry": json.loads(self.geometry.json)
        }
        if self.address:
            data["address"] = self.address.json

        return data

    def save(self, *args, **kwargs):
        if not self.address and not self.geometry:
            raise ValueError(_("At least Address field or Geometry "
                               "field has to be set"))
        super().save(*args, **kwargs)


class GenericNote(models.Model):
    activity_choices = []
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    activity = models.CharField(choices=activity_choices,
                                max_length=15)
    note = models.TextField(blank=True)


class Road(models.Model):

    class Meta:
        verbose_name = _("Silnice a dálnice")

    geometry = models.LineStringField(
            verbose_name=_("Geometrie"),
            help_text=_("Linie"),
            srid=4326)

    osm_id = models.CharField(
            max_length=256)
    code = models.IntegerField(blank=True)
    fclass = models.CharField(max_length=256)
    name = models.CharField(max_length=256, blank=True)
    ref = models.CharField(max_length=256, blank=True)
    oneway = models.BooleanField(default=False)
    maxspeed = models.IntegerField(blank=True)


class Airport(models.Model):

    geometry = models.PointField(
            verbose_name=_("Geometrie"),
            srid=4326)

    name = models.CharField(max_length=256)
    iata = models.CharField(max_length=4)


class PublicTransportStop(models.Model):

    geometry = models.PointField(
            verbose_name=_("Geometrie"),
            srid=4326)

    name = models.CharField(max_length=256)
    fclass = models.CharField(max_length=25)


class RailwayStation(models.Model):

    geometry = models.PointField(
            verbose_name=_("Geometrie"),
            srid=4326)

    name = models.CharField(max_length=256)
    fclass = models.CharField(max_length=25)
