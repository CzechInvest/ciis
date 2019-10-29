from django.db import models
from addresses.models import Address
from django.utils.translation import ugettext_lazy as _
import uuid


class Form(models.Model):
    form = models.TextField(max_length=32)

    def __str__(self):
        return self.form


class Ai(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(
        max_length=200,
        help_text=_("Name")
    )

    name_en = models.CharField(
        max_length=200,
        blank=True,
        help_text=_("Name (english)")
    )

    url = models.URLField(
            null=False,
            blank=False
    )

    form = models.ForeignKey(Form, on_delete=models.PROTECT)

    address = models.ForeignKey(Address,
                                on_delete=models.PROTECT)

    def __str__(self):
        return self.name
