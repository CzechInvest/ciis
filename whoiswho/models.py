from django.db import models
from contacts.models import ContactPerson
from cigeo.models import Location as GeoLocation
from django.utils import timezone


class Institution(models.Model):

    legal_form_choices = (
        ("POO", "Právnická osoba zapsaná v obchodním rejstříku"),
        ("VVS", "Veřejná nebo státní vysoká škola"),
        ("VVI", "Veřejná výzkumná instituce"),
        ("ZSP",
         "Zájmové sdružení právnických osob, občanské sdružení, spolek"),
    )
    name = models.CharField(max_length=256)
    name_en = models.CharField(max_length=256, blank=True)
    legal_form = models.CharField(max_length=8,
                                  chocies=legal_form_choices)
    ico = models.IntegerField()
    url = models.URLField()
    location = models.ForeignKey(GeoLocation)


class WhoIsWho(models.Model):

    institution = models.ForeignKey("Institution", on_delete=models.CASCADE)
    specialization = models.CharField(max_length=256)
    contact_person = models.ForeignKey("ContactPerson")
    keywords = models.ManyToManyField("Keyword")
    sectors = models.ManyToManyField("Sector")

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Institution, self).save(*args, **kwargs)


class Sector(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=256)


class Keyword(models.Model):
    kw = models.CharField(max_length=64)
