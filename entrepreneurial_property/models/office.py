from django.db import models
from .media import Water
from .media import Electricity
from .media import Gas
from .media import WasteWaterSevage
from .media import WasteWaterRain
from .media import WasteWaterIndustrial
from .media import Telecommunication

from .generic import Attachment
from .generic import Photo
from .generic import Location as EstateLocation
from cigeo.models import GenericNote as EstateNote


class OfficeTelecommunication(Telecommunication):

    green_field = models.OneToOneField(
        "Office",
        on_delete=models.CASCADE
    )


class OfficeWasteWaterSevage(WasteWaterSevage):
    diameter = capacity = None
    green_field = models.OneToOneField(
        "Office",
        on_delete=models.CASCADE
    )


class OfficeWasteWaterRain(WasteWaterRain):
    diameter = capacity = None
    green_field = models.OneToOneField(
        "Office",
        on_delete=models.CASCADE
    )


class OfficeWasteWaterIndustrial(WasteWaterIndustrial):
    diameter = capacity = None
    green_field = models.OneToOneField(
        "Office",
        on_delete=models.CASCADE
    )


class OfficeAttachment(Attachment):
    green_field = models.OneToOneField(
        "Office",
        on_delete=models.CASCADE
    )


class OfficePhoto(Photo):
    green_field = models.ForeignKey(
        "Office",
        on_delete=models.CASCADE
    )
    pass


class OfficeTechnologicalWater(Water):

    distance = None
    diameter = None
    capacity = None
    well = None
    well_capacity = None

    green_field = models.OneToOneField(
        "Office",
        on_delete=models.CASCADE
    )


class OfficeElectricity(Electricity):

    distance = None
    capacity = None
    current = None
    green_field = models.OneToOneField(
            "Office",
            on_delete=models.CASCADE
    )


class OfficeDrinkWater(Water):
    distance = None
    diameter = None
    capacity = None
    well = None
    well_capacity = None

    green_field = models.OneToOneField(
        "Office",
        on_delete=models.CASCADE
    )


class OfficeGas(Gas):
    diameter = pressure = capacity = None

    green_field = models.OneToOneField(
        "Office",
        on_delete=models.CASCADE
    )


class OfficeLocation(EstateLocation):

    green_field = models.OneToOneField(
        "Office",
        on_delete=models.CASCADE
    )


class OfficeGenericNote(EstateNote):

    green_field = models.ForeignKey(
        "Office",
        on_delete=models.CASCADE
    )
