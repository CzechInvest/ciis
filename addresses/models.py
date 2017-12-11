from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.

class Address(models.Model):
    adm = models.IntegerField(
            help_text='Kód ADM',
            primary_key=True)
    street = models.CharField(
            max_length = 200,
            help_text = "Ulice")
    number = models.CharField(
            max_length = 20,
            default=None,
            null=True,
            help_text = "Č.p.")
    city = models.ForeignKey("City",
            on_delete=models.PROTECT)
    zipcode = models.CharField(
            max_length = 200,
            help_text = "PSČ")

    coordinates = gis_models.PointField(
            null=True)

    def __str__(self):
        if self.street:
            street = self.street
        else:
            street = self.city
        return "{}, {}, {} - {}".format(street, self.number, self.zipcode, self.city)

class City(models.Model):
    code = models.IntegerField(
            unique=True,
            primary_key=True)
    name = models.CharField(
            max_length = 200,
            help_text = "Obec")

    def __str__(self):
        return self.name
