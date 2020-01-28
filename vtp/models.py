from django.db import models
from addresses.models import Address
from django.utils.translation import ugettext_lazy as _

class VtpType(models.Model):

    type = models.CharField(
            max_length=16
    )
    def __str__(self):

        return self.type


class Service(models.Model):

    service = models.CharField(
            max_length=128)

    def __str__(self):
        return self.service

class Vtp(models.Model):


    name = models.CharField(
            verbose_name=_("Název"),
            max_length=256
    )

    type = models.ManyToManyField(VtpType)

    services = models.ManyToManyField(Service)

    url = models.URLField()

    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name
