from django.db import models

from django.db import models
from django.contrib.gis.db import models as gis_models
from addresses.models import Address

class RK(models.Model):

    name = models.CharField(max_length=32)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    director = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
