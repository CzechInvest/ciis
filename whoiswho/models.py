from django.db import models
from contacts.models import ContactPerson as MyContactPerson
from addresses.models import Address
from django.utils import timezone


class WhoIsWho(models.Model):

    institution = models.ForeignKey("Institution",
                                    on_delete=models.CASCADE)
    specialization = models.CharField(max_length=256)
    contact_person = models.ForeignKey("ContactPerson",
                                       on_delete=models.PROTECT)
    keywords = models.ManyToManyField("Keyword")
    sectors = models.ManyToManyField("Sector")
    profile = models.TextField(blank=True)

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(WhoIsWho, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.institution.name,
                                self.specialization[0:20])


class ContactPerson(MyContactPerson):
    pass

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)


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
                                  choices=legal_form_choices)
    ico = models.CharField(max_length=8,)
    url = models.URLField()
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.name.replace("/", "\n ")[0:30]


class Sector(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=256)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return ""


class Keyword(models.Model):
    kw = models.CharField(max_length=64)

    def __str__(self):
        return self.kw
