from django.db import models
from addresses.models import Address
from contacts.models import ContactPerson

# Create your models here.
class Infrastructure(models.Model):

    name = models.CharField(
            max_length=200,
            help_text="Název",
            blank=False
    )

    inf_type = models.ManyToManyField("InfType")

    short_description = models.TextField(
            help_text="Stručný popis", blank=True)

    description = models.TextField(
            help_text="Popis", blank=True)

    address = models.ForeignKey(Address)

    industry = models.ManyToManyField("Industry")

    services = models.ManyToManyField("Service")

    year = models.IntegerField(
            help_text="Foundation year")

    url = models.URLField()

    twitter = models.URLField()
    facebook = models.URLField()
    linkedin = models.URLField()

    mentors = models.IntegerField(
            help_text="Number of mentors")

    seets = models.IntegerField(
            help_text="Maximum number of seets")

    in_incubation = models.IntegerField(
            help_text="Number of companies in incubation")

    conditions = models.TextField(
            help_text="Conditions for SUP (industry, stage etc.)")

    price = models.IntegerField(
            help_text="Seet/Month")

    note = models.TextField(
            help_text="Just some note")

    contact_person = models.ManyToManyField(ContactPerson)

    cooperation = models.ManyToManyField("Organisation")

    online_database = models.BooleanField()
    published = models.BooleanField()

    evaluation = models.TextField()


class Organisation(models.Model):

    name = models.CharField(
            max_length=100,
            help_text="Organisation name")

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
