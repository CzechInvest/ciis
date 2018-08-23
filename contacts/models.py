from django.db import models
from django.utils.translation import ugettext_lazy as _
from addresses.models import Address


class ContactPerson(models.Model):

    class Meta:
        abstract = True

    first_name = models.CharField(
            help_text="First name",
            max_length=20)

    last_name = models.CharField(
            help_text="Last name",
            max_length=20)

    role = models.CharField(
            help_text="Director, HR Manager, ...",
            max_length=20)

    crm = models.URLField(
            help_text=_("CRM link"))

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Owner(models.Model):

    class Meta:
        abstract = True

    PRIVATE = 0
    PUBLIC = 1
    COMBINED = 2

    ONE = 1
    TWO = 2
    MORE = 100

    type_choices = (
        (PRIVATE, _("Private")),
        (PUBLIC, _("Public")),
        (COMBINED, _("Combined")),
    )

    type = models.IntegerField(
        choices=type_choices,
        help_text=_("Ownership type"))

    name = models.CharField(
        max_length=32,
        help_text=_("Name"))

    owners_choices = (
        (ONE, _("One")),
        (TWO, _("Two")),
        (MORE, _("More")),
    )

    number_of_owners = models.IntegerField(
        choices=owners_choices,
        default=ONE,
        help_text=_("Name"))

    crm = models.URLField(
            help_text=_("CRM link"))

    def __str__(self):
        return "{}".format(self.name)


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
