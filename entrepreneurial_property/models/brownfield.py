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


class BrownfieldTelecommunication(Telecommunication):

    green_field = models.OneToOneField(
        "Brownfield",
        on_delete=models.CASCADE
    )


class BrownfieldWasteWater(WasteWater):
    green_field = models.OneToOneField(
        "Brownfield",
        on_delete=models.CASCADE
    )


class BrownfieldAttachment(Attachment):
    green_field = models.OneToOneField(
        "Brownfield",
        on_delete=models.CASCADE
    )


class BrownfieldPhoto(Photo):
    green_field = models.ForeignKey(
        "Brownfield",
        on_delete=models.CASCADE
    )
    pass


class BrownfieldTechnologicalWater(Water):

    green_field = models.OneToOneField(
        "Brownfield",
        on_delete=models.CASCADE
    )


class BrownfieldElectricity(Electricity):

    green_field = models.OneToOneField(
            "Brownfield",
            on_delete=models.CASCADE
    )


class BrownfieldDrinkWater(Water):
    green_field = models.OneToOneField(
        "Brownfield",
        on_delete=models.CASCADE
    )


class BrownfieldGas(Gas):
    green_field = models.OneToOneField(
        "Brownfield",
        on_delete=models.CASCADE
    )


class BrownfieldLocation(EstateLocation):

    green_field = models.OneToOneField(
        "Brownfield",
        on_delete=models.CASCADE
    )


class BrownfieldGenericNote(EstateNote):

    green_field = models.ForeignKey(
        "Brownfield",
        on_delete=models.CASCADE
    )
