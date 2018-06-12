from django.contrib.gis.db import models
from django.contrib.gis import geos
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
import requests
import time
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
        abstract = True


    address = models.ForeignKey(Address,
            null=True,
            blank=True,
            related_name="+",
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
            if self.address.house_number and \
                self.address.orientation_number:
                    hr = "{}/{}".format(self.address.house_number,
                            self.address.orientation_number)
            elif self.address.house_number:
                hr = self.address.house_number
            elif self.address.orientation_number:
                hr = orientation_number
            else:
                hr = ""

            return "{} {}, {}".format(self.address.street,
                    hr, self.address.city)
        else:
            lau1s = ", ".join([l.name for l in Lau1.objects.filter(geometry__intersects=self.geometry)])
            return lau1s

    @classmethod
    def create(self, *args, **kwargs):

        me = super(Location, self)(*args, **kwargs)
        me.highway_distance = self.get_highway_distance()
        return me

    def save(self, *args, **kwargs):

        if self.highway_distance == -1:
            self.highway_distance = self.get_highway_distance()
        super().save(*args, **kwargs)


    def get_highway_distance(self):

        centroid = self.geometry.centroid

        url = "https://router.project-osrm.org/route/v1/driving/{startx},{starty};{destx},{desty}?overview=simplified&geometries=geojson&steps=false"

        distances = []
        link = Road.objects.filter(
                fclass__contains="_link").filter(
                        geometry__distance_lte=(centroid,
                            D(m=100000))).annotate(distance=Distance('geometry',
                                centroid)).order_by('distance')[0]

        target = link.geometry.centroid
        target_url = url.format(startx=centroid.x, starty=centroid.y,
                                destx=target.x, desty=target.y)

        resp = requests.get(target_url)
        if resp.status_code == 200:
            data = resp.json()
            return data["routes"][0]["distance"]
        else:
            if (resp.status_code == 429):
                time.sleep(1)
                return self.get_highway_distance(objct)
            else:
                return -1

class Area(models.Model):
    class Meta:
        verbose_name = _("Rozloha plochy")
        verbose_name_plural = _("Rozloha ploch")
        abstract=True

    total = models.IntegerField(
            verbose_name=_('Celková rozloha'),
            help_text = _("Celková rozloha <code>m<sup>2</sup></code>"))
    free = models.IntegerField(
            verbose_name=_('Volná plocha'),
            help_text = _("Volná plocha <code>m<sup>2</sup></code>"))
    to_be_build = models.IntegerField(
            verbose_name=_('K zástavbě'),
            help_text = _("K zástavbě dle ÚP <code>m<sup>2</sup></code>"))
    for_expansion = models.IntegerField(
            verbose_name=_('K expanzi'),
            help_text = _("K expanzi <code>m<sup>2</sup></code>"))
    available_from = models.DateField(
            verbose_name=_('K dispozici od'),
            help_text = _("K dispozici od"))

    further_development = models.BooleanField(
        default=False,
        verbose_name=_('Možnost další expanze'),
    )

    further_development_description = models.TextField(
        blank=True,
        verbose_name=_('Možnost expanze - popis'),
    )

class Medium(models.Model):

    class Meta:
        abstract = True

    distance = models.IntegerField(
            verbose_name=_("Vzdálenost"),
            help_text="vzdálenost k objektu <code>[m]</code>")

    note = models.TextField(
            verbose_name=_("Poznámka"),
            help_text=_("Poznámka"))


class Water(Medium):

    class Meta:
        abstract = True

    diameter = models.IntegerField(
            verbose_name=_("Velikost přípojky"),
            help_text=_("Velikost přípojky <code>[mm]</code>"))
    well = models.IntegerField(
            verbose_name=_("Studna"),
            help_text=_("Studna <code>[m<sup>3</sup>]</code>"))
    capacity = models.IntegerField(
            verbose_name=_("Kapacita přípojky"),
            help_text=_("Kapacita přípojky <code>[m<sup>3</sup>/d]</code>"))
    well_capacity = models.IntegerField(
            verbose_name=_("Kapacita studny"),
            help_text=_("Kapacita studny <code>[m<sup>3</sup>/d]</code>"))

class Road(models.Model):

    class Meta:
        verbose_name=_("Silnice a dálnice")

    geometry = models.LineStringField(
            verbose_name=_("Geometrie"),
            help_text=_("Linie"),
            srid=4326)

    osm_id = models.CharField(
            max_length=256)
    code = models.IntegerField(blank=True)
    fclass = models.CharField(max_length=256)
    name = models.CharField(max_length=256, blank=True)
    ref = models.CharField( max_length=256, blank=True)
    oneway = models.BooleanField(default=False)
    maxspeed = models.IntegerField(blank=True)
