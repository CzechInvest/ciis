from django.db import models
from addresses.models import Address
from django.utils.translation import ugettext_lazy as _
import uuid
from django.core.exceptions import ValidationError

# Create your models here.

def is_year(value):
    if not 1700 < value < 2050:
        raise ValidationError(
            _('%(value)d does not seem tobe valid year'),
            params={'value': value},
        )

class Subject(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    ico = models.CharField(max_length=24,)
    url = models.URLField()
    address = models.ForeignKey(Address, blank=True, null=True,
                                on_delete=models.PROTECT)
    keywords = models.ManyToManyField("Keyword", blank=True)
    domain = models.ManyToManyField("Domain", blank=True)
    subdomain = models.ManyToManyField("Subdomain", blank=True)
    business_area = models.ManyToManyField("BusinessArea", blank=True)
    department = models.ForeignKey("Department", on_delete=models.PROTECT)
    note = models.TextField(blank=True, null=True)


    turnover = models.ForeignKey("Turnover", blank=True, null=True,
            on_delete=models.PROTECT)
    employees = models.ForeignKey("Employees", blank=True, null=True,
            on_delete=models.PROTECT)
    contact = models.ManyToManyField("Contact")
    profile = models.TextField(blank=True, null=True)

    #module = models.ManyToManyField("Module")
    ket = models.ManyToManyField("Ket", blank=True)
    nace = models.ManyToManyField("Nace", blank=True)

    TECHNOLOGY_LEVEL_CHOICES = (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
    )
    technology_readiness = models.IntegerField(null=True, blank=True,
            choices=TECHNOLOGY_LEVEL_CHOICES)
    year_founded = models.IntegerField("Year of foundation",
            null=True, blank=True, validators=[is_year])

    #destination = models.ManyToManyField("Destination")
    #programm = models.ManyToManyField("Programm")

class Programm(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Contact(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    voicephone = models.CharField(max_length=256)
    department = models.ManyToManyField("Department")


class Keyword(models.Model):
    kw = models.CharField(max_length=256)

    def __str__(self):
        return self.kw

class Nace(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    nace = models.CharField(max_length=256)

    def __str__(self):
        return "{} {}".format(self.id, self.nace)

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

class BusinessArea(models.Model):
    business_area = models.CharField(max_length=256)

    def __str__(self):
        return self.business_area

class Domain(models.Model):
    domain = models.CharField(max_length=256)

    def __str__(self):
        return self.domain

class Subdomain(models.Model):
    subdomain = models.CharField(max_length=256)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

    def __str__(self):
        return self.subdomain

class Department(models.Model):
    abbr = models.CharField(max_length=4)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
