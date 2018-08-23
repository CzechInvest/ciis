import requests
import time
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.contrib.gis.measure import D
from django.db import models
from django.contrib.gis import geos
from django.contrib.gis.geos import *
from django.contrib.gis.db.models.functions import Distance
from cigeo.models import Location as GenericLocation
from cigeo.models import Road
from cigeo.models import RailwayStation
from cigeo.models import Airport
from cigeo.models import PublicTransportStop


class Attachment(models.Model):

    class Meta:
        abstract = True

    title = models.CharField(
        max_length=200,
        help_text=_("Title"))

    description = models.TextField(
        help_text=_("Description"),
        null=True,
        blank=True)

    attachment = models.FileField(
        help_text=_("Attachment file")
    )


class Photo(models.Model):

    class Meta:
        abstract = True

    title = models.CharField(
        max_length=200,
        help_text=_("Photo title")
    )

    description = models.TextField(
        help_text=_("Description"),
        null=True,
        blank=True)

    image = models.ImageField(
        help_text=_("Image file")
    )


class Location(GenericLocation):

    class Meta:
        abstract = True

    highway_distance = models.FloatField(default=-1)
    airport_distance = models.FloatField(default=-1)
    public_transport_distance = models.FloatField(default=-1)
    railway_distance = models.FloatField(default=-1)

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

        if self.highway_distance < 0:
            self.highway_distance = self.get_distance_to("highway")

        if self.airport_distance < 0:
            self.airport_distance = self.get_distance_to("airport")

        if self.public_transport_distance < 0:
            self.public_transport_distance = self.get_distance_to("public_transport")

        if self.railway_distance < 0:
            self.railway_distance = self.get_distance_to("railway")

        super().save(*args, **kwargs)

    def get_distance_to(self, to):
        """Distance to certain point on the road network"""

        centroid = self.geometry.centroid

        url = "https://router.project-osrm.org/route/v1/driving/{startx},{starty};{destx},{desty}?overview=simplified&geometries=geojson&steps=false"

        link = self.get_closest_point(to)

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
                return self.get_distance_to(to)
            else:
                return -1

    def get_closest_point(self, to):

        centroid = self.geometry.centroid

        if to == "highway":
            distances = Road.objects.filter(
                Q(fclass__contains="highway_link") |
                Q(fclass__contains="trunk_link") |
                Q(fclass__contains="motorway_link")
            ).filter(
                geometry__distance_lte=(
                    centroid,
                    D(m=100000)
                )
            )

        elif to == "airport":
            distances = Airport.objects.filter(
                geometry__distance_lte=(
                    centroid,
                    D(m=500000)
                )
            )

        elif to == "public_transport":
            distances = PublicTransportStop.objects.all().filter(
                geometry__distance_lte=(
                    centroid,
                    D(m=10000)
                )
            )

        elif to == "railway":
            distances = RailwayStation.objects.all().filter(
                geometry__distance_lte=(
                    centroid, D(m=50000)))

        link = distances.annotate(
            distance=Distance(
                'geometry',
                centroid
            )
        ).order_by('distance')[0]

        return link
