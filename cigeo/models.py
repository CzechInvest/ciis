from django.contrib.gis.db import models
from django.contrib.gis import geos
from addresses.models import Address
import shapely.wkt
from django.utils.translation import ugettext_lazy as _

class Nuts3(models.Model):

    class meta:
        verbose_name = _("Kraj (NUTS3)")
        verbose_name_plural = _("Kraje (NUTS3)")

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


class Lau1(models.Model):
    # okresy

    class meta:
        verbose_name = _("Okres (LAU1)")
        verbose_name_plural = _("Okresy (LAU1)")

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


class Location(models.Model):

    class Meta:
        verbose_name=_("Umístění")
        verbose_name_plural=_("Umístění")


    address = models.ForeignKey(Address,
            null=True,
            blank=True,
            verbose_name=_("Adresa"),
            on_delete=models.SET_NULL)
    geometry = models.GeometryCollectionField(
            verbose_name=_("Geometrie"),
            help_text=_("Body, linie, polygony"),
            null=True,
            blank=True,
            srid=4326)

    def save(self, *args, **kwargs):
        """Save location object

        This method convert's address.geometry and appends it to geometry
        """

        if self.address and self.geometry:
            if not self.address.coordinates.intersects(self.geometry):
                self.geometry.append(self.address.coordinates)
        elif self.address:

            gc = geos.GeometryCollection([self.address.coordinates])
            self.geometry = gc

        super().save(*args, **kwargs)

    def __str__(self):
        if self.address:
            return "{} {}, {}".format(self.address.street, self.address.number,
                    self.address.city)
        else:
            lau1s = ", ".join([l.name for l in Lau1.objects.filter(geometry__intersects=self.geometry)])
            return lau1s
