from django.db import models
from addresses.models import Address
from django.utils.translation import ugettext_lazy as _


class ContactPerson(models.Model):

    class Meta:
        abstract = True

    first_name = models.CharField(
            help_text="First name",
            max_length=20)

    middle_name = models.CharField(
            help_text="Middle name",
            null=True,
            blank=True,
            max_length=20)

    last_name = models.CharField(
            help_text="Last name",
            max_length=20)

    titles = models.CharField(
            help_text="Mgr., PhDr., MUDr., Ing., PhD., ...",
            null=True,
            blank=True,
            max_length=20)

    email = models.EmailField()

    phone = models.CharField(
            max_length=20)

    role = models.CharField(
            help_text="Director, HR Manager, ...",
            max_length=20)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Organisation(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(
        help_text=_("Organisation name"),
        max_length=128)

    regid = models.CharField(
        unique=True,
        help_text=_("Registration ID (IČO)"),
        max_length=16)

    regid = models.CharField(
            help_text=_("Registration ID (IČO)"),
            max_length=16)

    address = models.ForeignKey(Address,
                                on_delete=models.CASCADE)

    note = models.TextField(
            blank=True,
            help_text=_("Note"))

    crm = models.URLField(
            help_text=_("CRM"))
