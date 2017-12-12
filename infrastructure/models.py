from django.db import models
from addresses.models import Address
from contacts.models import ContactPerson

# Create your models here.
class Infrastructure(models.Model):

    name = models.CharField(
            max_length=200,
            help_text="Název",
            null=False,
            blank=False
    )

    logo = models.ImageField(
            help_text="Logo",
            blank=True,
            null=True
    )

    inf_type = models.ManyToManyField("InfType")

    description_cz = models.TextField(
            help_text="Popis [cz]",
            null=False,
            blank=False)

    description_en = models.TextField(
            help_text="Popis [en]", blank=True)

    address = models.ForeignKey(Address,
            on_delete=models.PROTECT)

    industry = models.ManyToManyField("Industry")

    services = models.ManyToManyField("Service")

    year = models.IntegerField(
            blank=True,
            help_text="Foundation year")

    url = models.URLField(
            null=False,
            blank=False
    )

    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    mentors = models.IntegerField(
            blank=True,
            help_text="Number of mentors")

    seats = models.IntegerField(
            blank=True,
            help_text="Maximum number of seets")

    in_incubation = models.IntegerField(
            blank=True, null=True,
            help_text="Number of companies in incubation")

    conditions = models.TextField(
            blank=True,
            help_text="Conditions for SUP (industry, stage etc.)")

    price = models.IntegerField(
            blank=True,
            help_text="Seet/Month")

    note = models.TextField(
            blank=True, null=True,
            help_text="Just some note")

    contact_person = models.ManyToManyField(ContactPerson,
            blank=True,
            null=True)

    cooperation = models.ManyToManyField("Organisation",
            blank=True,
            null=True)

    def __str__(self):
        return self.name

class Organisation(models.Model):

    name = models.CharField(
            max_length=100,
            help_text="Organisation name")

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(
            help_text="Services provided",
            max_length = 20)

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(
            help_text="Industry name",
            max_length =20)


    def __str__(self):
        return self.name

class InfType(models.Model):

    name = models.CharField(
            help_text="Typ",
            max_length=20,
            blank=False,
            choices=(
                ("inc", "Incubator"),
                ("vtp", "VTP"),
                ("coow", "Co-working"),
                ("acc", "Accelerator"),
            )
    )

    def __str__(self):
        return self.name
