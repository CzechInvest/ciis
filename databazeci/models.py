from django.db import models
from addresses.models import Address
from django.utils.translation import ugettext_lazy as _
import uuid

# Create your models here.

class Subject(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    ico = models.CharField(max_length=24,)
    url = models.URLField()
    address = models.ForeignKey(Address, blank=True, null=True,
                                on_delete=models.PROTECT)
    keywords = models.ManyToManyField("Keyword")
    domain = models.ManyToManyField("Domain")
    subsector = models.ManyToManyField("Subsector")
    department = models.ManyToManyField("Department")
    note = models.TextField(blank=True)


    turnover = models.ForeignKey("Turnover", on_delete=models.PROTECT)
    employees = models.ForeignKey("Employees", on_delete=models.PROTECT)
    contact = models.ForeignKey("Contact", blank=True, null=True, on_delete=models.PROTECT)
    profile = models.TextField(blank=True)

    module = models.ManyToManyField("Module")
    ket = models.ManyToManyField("Ket")
    nace = models.ForeignKey("Nace", on_delete=models.PROTECT)

class Contact(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    voicephone = models.CharField(max_length=256)


class Keyword(models.Model):
    kw = models.CharField(max_length=256)

    def __str__(self):
        return self.kw

class Nace(models.Model):
    nace = models.CharField(max_length=256)

    def __str__(self):
        return self.nace

class Ket(models.Model):
    ket = models.CharField(max_length=256)

    def __str__(self):
        return self.ket

class Module(models.Model):
    module = models.CharField(max_length=256)
    sector = models.ForeignKey("Sector", on_delete=models.PROTECT)

    def __str__(self):
        return "{} | {}".format(self.sector, self.module)

class Sector(models.Model):
    sector = models.CharField(max_length=256)

    def __str__(self):
        return self.sector

class Turnover(models.Model):
    upto = models.IntegerField()
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.description

class Employees(models.Model):
    upto = models.IntegerField()
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.description

class Domain(models.Model):
    domain = models.CharField(max_length=256)

    def __str__(self):
        return self.domain

class Subsector(models.Model):
    sector = models.CharField(max_length=256)

    def __str__(self):
        return self.sector

class Department(models.Model):
    abbr = models.CharField(max_length=4)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.sector
