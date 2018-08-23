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


class GreenFieldTelecommunication(Telecommunication):

    green_field = models.OneToOneField(
        "GreenField",
        on_delete=models.CASCADE
    )


class GreenFieldWasteWaterSevage(WasteWaterSevage):
    green_field = models.OneToOneField(
        "GreenField",
        on_delete=models.CASCADE
    )


class GreenFieldWasteWaterRain(WasteWaterRain):
    green_field = models.OneToOneField(
        "GreenField",
        on_delete=models.CASCADE
    )


class GreenFieldWasteWaterIndustrial(WasteWaterIndustrial):
    green_field = models.OneToOneField(
        "GreenField",
        on_delete=models.CASCADE
    )


class GreenFieldAttachment(Attachment):
    green_field = models.OneToOneField(
        "GreenField",
        on_delete=models.CASCADE
    )


class GreenFieldPhoto(Photo):
    green_field = models.ForeignKey(
        "GreenField",
        on_delete=models.CASCADE
    )
    pass


class GreenFieldTechnologicalWater(Water):

    green_field = models.OneToOneField(
        "GreenField",
        on_delete=models.CASCADE
    )


class GreenFieldElectricity(Electricity):

    green_field = models.OneToOneField(
            "GreenField",
            on_delete=models.CASCADE
    )


class GreenFieldDrinkWater(Water):
    green_field = models.OneToOneField(
        "GreenField",
        on_delete=models.CASCADE
    )


class GreenFieldGas(Gas):
    green_field = models.OneToOneField(
        "GreenField",
        on_delete=models.CASCADE
    )


class GreenFieldLocation(EstateLocation):

    green_field = models.OneToOneField(
        "GreenField",
        on_delete=models.CASCADE
    )


class GreenFieldGenericNote(EstateNote):

    green_field = models.ForeignKey(
        "GreenField",
        on_delete=models.CASCADE
    )
