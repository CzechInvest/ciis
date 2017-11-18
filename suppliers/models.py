from django.db import models
from addresses.models import Address
from contacts.models import ContactPerson

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(
            max_length=200,
            help_text="Název dodavatele",
            blank=False
    )
    regid = models.IntegerField(
            help_text="IČO",
            blank=False
    )

    address = models.ForeignKey(Address)

    phone = models.CharField(
            max_length=20,
            help_text="Telefon")

    fax = models.CharField(
            max_length=20,
            help_text="Fax")

    email = models.EmailField()

    url = models.URLField()

    sectors = models.ManyToManyField('Sector')

    join_venture = models.BooleanField(
            help_text="Join-venture",
            default=False,
            blank=False)

    custom_made = models.BooleanField(
            help_text="Zakázková výroa",
            default=False,
            blank=False)

    capital = models.BooleanField(
            help_text="Zahraniční kapitál",
            default=False,
            blank=False)

    turnover = models.IntegerField(
            help_text="Obrat [€]",
            blank=False)

    export = models.FloatField(
            help_text="Export [%]",
            blank=False)

    employes = models.IntegerField(
            help_text="Počet zaměstnanců",
            blank=False)

    year = models.IntegerField(
            help_text="Rok založení",
            blank=False)

    main_activity = models.CharField(
            max_length=200,
            help_text="Hlavní činnost")

    certificates = models.ManyToManyField("Certificate")

    contact_person = models.ManyToManyField(ContactPerson)


class Sector(models.Model):
    name = models.CharField(
            max_length=200,
            unique=True,
            help_text="Sektor")

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name=models.CharField(help_text="Certifikát",
            unique=True,
            max_length=20)

    def __str__(self):
        return self.name
