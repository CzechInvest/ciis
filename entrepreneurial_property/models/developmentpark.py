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


class DevelopmentParkTelecommunication(Telecommunication):

    green_field = models.OneToOneField(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )


class DevelopmentParkWasteWaterSevage(WasteWaterSevage):
    green_field = models.OneToOneField(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )


class DevelopmentParkWasteWaterRain(WasteWaterRain):
    green_field = models.OneToOneField(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )


class DevelopmentParkWasteWaterIndustrial(WasteWaterIndustrial):
    green_field = models.OneToOneField(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )


class DevelopmentParkAttachment(Attachment):
    green_field = models.OneToOneField(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )


class DevelopmentParkPhoto(Photo):
    green_field = models.ForeignKey(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )
    pass


class DevelopmentParkTechnologicalWater(Water):

    green_field = models.OneToOneField(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )


class DevelopmentParkElectricity(Electricity):

    green_field = models.OneToOneField(
            "DevelopmentPark",
            on_delete=models.CASCADE
    )


class DevelopmentParkDrinkWater(Water):
    green_field = models.OneToOneField(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )


class DevelopmentParkGas(Gas):
    green_field = models.OneToOneField(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )


class DevelopmentParkLocation(EstateLocation):

    green_field = models.OneToOneField(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )


class DevelopmentParkGenericNote(EstateNote):

    green_field = models.ForeignKey(
        "DevelopmentPark",
        on_delete=models.CASCADE
    )
