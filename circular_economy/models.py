from django.db import models
from addresses.models import Address
from contacts.models import ContactPerson as MyContactPerson
from django.utils.translation import ugettext_lazy as _
import uuid


class ContactPerson(MyContactPerson):
    pass


class Keyword(models.Model):
    keyword = models.TextField(max_length=32)


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=200,
        help_text=_("Name")
    )

    url = models.URLField(
            null=False,
            blank=False
    )

    contact_person = models.ForeignKey(ContactPerson, on_delete=models.PROTECT)

    address = models.ForeignKey(Address,
                                on_delete=models.PROTECT)

    characteristics = models.TextField()


class Municipality(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=200,
        help_text=_("Name")
    )

    activity = models.CharField(
        max_length=200,
        help_text=_("Activity name")
    )

    url = models.URLField(
            null=False,
            blank=False
    )
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.PROTECT)
    address = models.ForeignKey(Address,
                                on_delete=models.PROTECT)
    characteristics = models.TextField()
    project_description = models.TextField()
    challange = models.TextField()
    result = models.TextField()
    keywords = models.ManyToManyField("Keyword")


class Pilot(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=200,
        help_text=_("Name")
    )

    activity = models.CharField(
        max_length=200,
        help_text=_("Activity name")
    )

    url = models.URLField(
            null=False,
            blank=False
    )
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.PROTECT)
    address = models.ForeignKey(Address,
                                on_delete=models.PROTECT)
    characteristics = models.TextField()
    project_description = models.TextField()
    challange = models.TextField()
    result = models.TextField()
    keywords = models.ManyToManyField("Keyword")
