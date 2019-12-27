from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class KodSed(models.Model):
    kod = models.IntegerField()

    def __str__(self):
        return str(self.kod)


class OP(models.Model):
    op = models.CharField(
            max_length=16
    )

    def __str__(self):
        return str(self.op)


class Field(models.Model):
    field = models.CharField(
            max_length=16)

    def __str__(self):
        return str(self.field)


class DataSource(models.Model):
    source = models.CharField(
            max_length=16)

    def __str__(self):
        return self.source


class Indicator(models.Model):

    kod_nci_07_13 = models.CharField(
        null=True,
        blank=True,
        max_length=16,
        verbose_name=_("kód NČI 07-13")
    )

    npr_envi = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=_("NPR/ENVI")
    )
    c_s = models.CharField(
            null=True,
            blank=True,
            max_length=1,
            verbose_name=_("C/S"),
            choices=(
                ("c", "C"),
                ("s", "S")
                )
            )

    fond = models.CharField(
            null=True,
            blank=True,
            verbose_name=_("Fond"),
            max_length=16,
            choices=(
                ("efrr_fs", "EFRR / FS"),
                ("enrf", "ENRF"),
                ("esf", "ESF"),
                ("esf_yei", "ESF / YEI"),
                ("eus", "EUS"),
                ("ezfrv", "EZFRV"),
                )
            )

    kod_ek = models.CharField(
            null=True,
            blank=True,
            max_length=16)

    wf = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("WF"),
    )

    kod_nci_2014 = models.CharField(
            max_length=16,
            verbose_name=_("KódNČI2014+"),
            null=True,
            blank=True)

    kod_sfc = models.CharField(
            null=True,
            blank=True,
            verbose_name=_("Kód v SFC"),
            max_length=16)

    kod_sed = models.ManyToManyField(
            KodSed,
            verbose_name=_("Kód SED"),
            blank=True)

    op = models.ManyToManyField(
            OP,
            related_name="%(class)s_op",
            verbose_name=_("OP"),
            blank=True)

    main_indicator = models.ManyToManyField(
            OP,
            related_name="%(class)s_main_indicator",
            verbose_name=_("Hlavní indikátor"),
            blank=True)

    sfc = models.ManyToManyField(
            OP,
            verbose_name=_("SFC"),
            blank=True)

    field = models.ManyToManyField(
            Field,
            verbose_name=_("Oblast"),
            blank=True)

    indicator_name_cs = models.TextField(
            verbose_name=_("Název indikátoru (CS)"))
    indicator_name_en = models.TextField(
            verbose_name=_("Název indikátoru (EN)"))
    unit = models.CharField(
            max_length=8,
            verbose_name=_("Měrná jednotka"))

    type = models.CharField(
            max_length=8,
            verbose_name=_("Typ"),
            choices=(
                ("context", "Kontext"),
                ("output", "Výstup"),
                ("result", "Výsledek")
                )
            )

    definition = models.TextField(
            verbose_name=_("Definice")
    )
    frequency = models.CharField(
            verbose_name=_("Frekvence"),
            max_length=16
            )

    resource = models.URLField(
            null=True,
            blank=True,
            verbose_name=_("Odkaz na zdroj dat")
            )

    resource_comments = models.CharField(
            null=True,
            blank=True,
            verbose_name=_("Zdroj metodiky / komentáře"),
            max_length=256
            )

    data_source = models.ForeignKey(
            DataSource,
            on_delete=models.PROTECT,
            verbose_name=_("Zdroj dat (Ž/P, ŘO, statistika"),
            )

    es_esf2014 = models.BooleanField(
            null=True,
            blank=True,
            verbose_name=_("Přenos do IS ESF2014+")
            )

    projects_number = models.IntegerField(
            null=True,
            blank=True,
            verbose_name=_("Počet Projektů")
            )

    ec_comments = models.TextField(
            null=True,
            blank=True,
            verbose_name=_("Comments EK"))
