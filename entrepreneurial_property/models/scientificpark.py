from django.db import models
from .media import Water
from .media import Electricity
from .media import Gas
from .media import WasteWater
from .media import Telecommunication

from .generic import Attachment
from .generic import Photo
from .generic import Location as EstateLocation
from cigeo.models import GenericNote as EstateNote


class ScientificParkTelecommunication(Telecommunication):

    green_field = models.OneToOneField(
        "ScientificPark",
        on_delete=models.CASCADE
    )


class ScientificParkWasteWater(WasteWater):
    diameter = capacity = None
    green_field = models.OneToOneField(
        "ScientificPark",
        on_delete=models.CASCADE
    )


class ScientificParkAttachment(Attachment):
    green_field = models.OneToOneField(
        "ScientificPark",
        on_delete=models.CASCADE
    )


class ScientificParkPhoto(Photo):
    green_field = models.ForeignKey(
        "ScientificPark",
        on_delete=models.CASCADE
    )
    pass


class ScientificParkTechnologicalWater(Water):

    distance = None
    diameter = None
    capacity = None
    well = None
    well_capacity = None

    green_field = models.OneToOneField(
        "ScientificPark",
        on_delete=models.CASCADE
    )


class ScientificParkElectricity(Electricity):

    distance = None
    capacity = None
    current = None
    green_field = models.OneToOneField(
            "ScientificPark",
            on_delete=models.CASCADE
    )


class ScientificParkDrinkWater(Water):
    distance = None
    diameter = None
    capacity = None
    well = None
    well_capacity = None

    green_field = models.OneToOneField(
        "ScientificPark",
        on_delete=models.CASCADE
    )


class ScientificParkGas(Gas):
    diameter = pressure = capacity = None

    green_field = models.OneToOneField(
        "ScientificPark",
        on_delete=models.CASCADE
    )


class ScientificParkLocation(EstateLocation):

    green_field = models.OneToOneField(
        "ScientificPark",
        on_delete=models.CASCADE
    )


class ScientificParkGenericNote(EstateNote):

    green_field = models.ForeignKey(
        "ScientificPark",
        on_delete=models.CASCADE
    )
