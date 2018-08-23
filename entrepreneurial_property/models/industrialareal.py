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


class IndustrialArealTelecommunication(Telecommunication):

    green_field = models.OneToOneField(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )


class IndustrialArealWasteWaterSevage(WasteWaterSevage):
    green_field = models.OneToOneField(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )


class IndustrialArealWasteWaterRain(WasteWaterRain):
    green_field = models.OneToOneField(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )


class IndustrialArealWasteWaterIndustrial(WasteWaterIndustrial):
    green_field = models.OneToOneField(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )


class IndustrialArealAttachment(Attachment):
    green_field = models.OneToOneField(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )


class IndustrialArealPhoto(Photo):
    green_field = models.ForeignKey(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )
    pass


class IndustrialArealTechnologicalWater(Water):

    green_field = models.OneToOneField(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )


class IndustrialArealElectricity(Electricity):

    green_field = models.OneToOneField(
            "IndustrialAreal",
            on_delete=models.CASCADE
    )


class IndustrialArealDrinkWater(Water):
    green_field = models.OneToOneField(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )


class IndustrialArealGas(Gas):
    green_field = models.OneToOneField(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )


class IndustrialArealLocation(EstateLocation):

    green_field = models.OneToOneField(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )


class IndustrialArealGenericNote(EstateNote):

    green_field = models.ForeignKey(
        "IndustrialAreal",
        on_delete=models.CASCADE
    )
