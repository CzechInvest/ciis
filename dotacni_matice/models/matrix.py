from django.db import models
from django.utils.translation import ugettext_lazy as _

MAX_SUPPORT = (
        (10, 10),
        (15, 15),
        (20, 20),
        (30, 30),
        (30, 35),
        (40, 40),
        (45, 45),
        (50, 50),
        (55, 55),
        (60, 60),
        (65, 65),
        (70, 70),
        (75, 75),
        (80, 80),
        (85, 85),
        (90, 90),
        (95, 95),
        (100, 100),
        (1, _("Ano")),
        (-1, _("Není stanoveno")),
        (-2, _("Dle aktivity")),
        (-3, _("Nelze určit")),
        )

STATE = (
        (10, _("Plánováno")),
        (20, _("Sběr plná")),
        (30, _("Vyhlášeno")),
        (40, _("Ukončeno"))
        )


class Competence(models.Model):

    competence = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.competence


class Program(models.Model):

    program = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.program


class CallType(models.Model):

    type = models.CharField(max_length=32)

    def __str__(self):
        return self.type


class DotacniTitul(models.Model):

    changed = models.DateField(
        auto_now=True,
        help_text=_("Changed")
    )

    competence = models.ForeignKey(
        Competence,
        null=True,
        on_delete=models.PROTECT
    )

    program = models.ForeignKey(
            Program,
            on_delete=models.PROTECT)

    name = models.CharField(max_length=256)

    type = models.ForeignKey(
            CallType,
            blank=True,
                null=True,
            on_delete=models.PROTECT)

    area=models.CharField(max_length=256, null=True, blank=True)

    mip = models.IntegerField(blank=True,
                null=True,
                choices=MAX_SUPPORT)
    mp = models.IntegerField(blank=True,
                null=True,
                choices=MAX_SUPPORT)
    sp = models.IntegerField(blank=True,
                null=True,
                choices=MAX_SUPPORT)
    vp = models.IntegerField(blank=True,
                null=True,
                choices=MAX_SUPPORT)
    nno = models.IntegerField(blank=True,
                null=True,
                choices=MAX_SUPPORT)
    public = models.IntegerField(blank=True,
                null=True,
                choices=MAX_SUPPORT)

    #state = models.IntegerField(blank=False,
    #            choices=STATE)

    date_call = models.DateField(
            null=True,
            blank=True)
    date_pref_from = models.DateField(
            null=True,
            blank=True)
    date_pref_to = models.DateField(
            null=True,
            blank=True)
    date_full_from = models.DateField(
            null=True,
            blank=True)
    date_full_to = models.DateField(
            null=True,
            blank=True)
    allocated = models.IntegerField(
            blank=True, null=True,
            help_text=_("[*10^6 Kč]"))
    min = models.IntegerField(
            blank=True,
            null=True,
            help_text=_("[*10^6 Kč]"))
    max = models.IntegerField(
            blank=True,
            null=True,
            help_text=_("[*10^6 Kč]"))
    form = models.CharField(
            blank=True,
                null=True,
            max_length=64)
    history = models.TextField(
            blank=True,
                null=True)
    regime = models.CharField(
            blank=True,
                null=True,
            max_length=64)

    supported_activities = models.TextField(
            null=True,
            blank=True)

    eligible_costs = models.TextField(
            null=True,
            blank=True)
    ineligible_costs = models.TextField(
            null=True,
            blank=True)
    pkn = models.IntegerField(blank=True, null=True)
    pkv = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True, max_length=256)
    comment = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    afc = models.BooleanField(blank=True, null=True)
    ipo = models.BooleanField(blank=True, null=True)

    investment = models.BooleanField(blank=True, null=True)
    noninvestment = models.BooleanField(blank=True, null=True)
    remuneration = models.BooleanField(blank=True, null=True)
    personal_costs = models.BooleanField(blank=True, null=True)
    education = models.BooleanField(blank=True, null=True)
    consultation = models.BooleanField(blank=True, null=True)
    research = models.BooleanField(blank=True, null=True)
    property = models.BooleanField(blank=True, null=True)
    machines = models.BooleanField(blank=True, null=True)
    construction = models.BooleanField(blank=True, null=True)
    administration = models.BooleanField(blank=True, null=True)
    hw = models.BooleanField(blank=True, null=True)
    sw = models.BooleanField(blank=True, null=True)
    lump = models.BooleanField(blank=True, null=True)
    marketing = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.name
