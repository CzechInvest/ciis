from django.db import models
from contacts.models import ContactPerson as MyContactPerson
from contacts.models import Organisation as MyOrganisation
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db import models as gis_models


# Create your models here.
class Supplier(models.Model):

    id = models.IntegerField(default=-1, primary_key=True)

    name = models.TextField(
            help_text=_("Name"), blank=True)

    address = models.TextField(
            help_text=_("Adresa"),
            blank=True)

    ico = models.TextField(
            help_text=_("IČO"),
            blank=True)

    url = models.URLField(
            help_text=_("URL"),
            blank=True)

    core_business = models.TextField(
            help_text=_("Core business"),
            blank=True)

    geom = gis_models.PointField(
            help_text=_("Bod"),
            blank=True)

    def __str__(self):
        return self.name

    class Meta():
        managed = False
        db_table = 'domino\".\"suppliers'
