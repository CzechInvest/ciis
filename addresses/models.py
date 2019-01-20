from django.db import models
from django.contrib.gis.db import models as gis_models
import json

# Create your models here.

class Address(models.Model):
    adm = models.IntegerField(
            help_text='Kód ADM',
            primary_key=True)
    street = models.CharField(
            max_length = 200,
            help_text = "Ulice")
    house_number = models.CharField(
            max_length = 20,
            default=None,
            null=True,
            help_text = "Domovní číslo")
    orientation_number = models.CharField(
            max_length = 20,
            default=None,
            null=True,
            help_text = "Orientační číslo")
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    zipcode = models.CharField(
            max_length = 200,
            help_text = "PSČ")

    coordinates = gis_models.PointField(
            null=True)

    @property
    def number(self):
        slash = ""
        if self.orientation_number:
            slash = "/"
        return "{}{}{}".format(
            self.house_number,
            slash,
            self.orientation_number
        )

    def __str__(self):
        if self.street:
            street = self.street
        else:
            street = self.city
        return "{}, {}, {} - {}".format(street, self.number,
                                        self.zipcode, self.city)

    @property
    def json(self):
        return {
            "adm": self.adm,
            "street": self.street,
            "house_number": self.house_number,
            "orientation_number": self.orientation_number,
            "city": self.city.name,
            "zipcode": self.zipcode,
            "coordinates": json.loads(self.coordinates.json)
        }

class City(models.Model):
    code = models.IntegerField(
            unique=True,
            primary_key=True)
    name = models.CharField(
            max_length = 200,
            help_text = "Obec")

    def __str__(self):
        return self.name
