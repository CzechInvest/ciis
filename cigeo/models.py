from django.contrib.gis.db import models
from django.contrib.gis import geos
from addresses.models import Address
import shapely.wkt

class Location(models.Model):

    address = models.ForeignKey(Address,
            null=True,
            blank=True,
            on_delete=models.SET_NULL)
    geometry = models.GeometryCollectionField(
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
            return "Geometrická kolekce"
