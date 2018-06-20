from django.db import models
from contacts.models import ContactPerson as MyContactPerson
from contacts.models import Organisation as MyOrganisation
from django.utils.translation import ugettext_lazy as _
from addresses.models import Address


# Create your models here.
class Supplier(models.Model):

    name = models.CharField(
            max_length=200,
            help_text="Název dodavatele",
            blank=False
    )

    join_venture = models.BooleanField(
            help_text=_("Join-venture"),
            default=False,
            blank=False)

    custom_made = models.BooleanField(
            help_text=_("Zakázková výroba"),
            default=False,
            blank=False)

    capital = models.BooleanField(
            help_text=_("Zahraniční kapitál"),
            default=False,
            blank=False)

    turnover = models.IntegerField(
            help_text=_("Obrat [€]"),
            blank=False)

    export = models.FloatField(
            help_text=_("Export [%]"),
            blank=False)

    employes = models.IntegerField(
            help_text=_("Počet zaměstnanců"),
            blank=False)

    established = models.IntegerField(
            help_text=_("Rok založení"),
            blank=False)

    main_activity = models.CharField(
            max_length=200,
            help_text=_("Hlavní činnost"))

    certificates = models.ManyToManyField("Certificate")

    sectors = models.ManyToManyField('Sector')

    def __str__(self):
        return self.name


class Location(models.Model):

    class Meta:
        verbose_name = _("Lokace")
        verbose_name_plural = _("Lokace")

    address = models.ForeignKey(Address,
                                on_delete=models.CASCADE)
    supplier = models.ForeignKey('Supplier',
                                 on_delete=models.CASCADE)


class ContactPerson(MyContactPerson):
    organisation = models.OneToOneField(
        "Organisation",
        on_delete=models.CASCADE)


class Organisation(MyOrganisation):
    supplier = models.OneToOneField(
        "Supplier",
        on_delete=models.CASCADE)


class Sector(models.Model):
    name = models.CharField(
            max_length=200,
            unique=True,
            help_text="Sektor")

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(
        help_text="Certifikát",
        unique=True,
        max_length=20)

    def __str__(self):
        return self.name
