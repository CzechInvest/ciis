from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.

from .models.matrix import *
from .models.indicators import *

class DotacniTitulAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            "fields": ("competence",),
        }),
        (_("Výzva"), {
            "fields": ("program", "name", "type")
        }),
        (None, {
            "fields": ("area",),
        }),
        (_("Max. podpor % (o.spol. + NNO"), {
            "fields": ("mip", "mp", "sp", "vp", "nno", "public"),
        }),
        (None, {
            "fields": ("state",),
        }),
        (_("Termíny vyhl. / příjem předb. / plných"), {
            "fields": ("date_call", "date_pref_from", "date_pref_to",
                "date_full_from", "date_full_to"),
        }),
        (_("CZV / mil. Kč"), {
            "fields": ("allocated", "min", "max", "form")
        }),
        (None, {
            "fields": ("history", "regime", "supported_activities"),
        }),
        (_("Výdaje"), {
            "fields": ("eligible_costs", "ineligible_costs", "pkn", "pkv"),
        }),
        (None, {
            "fields": ("url", "comment", "note"),
        }),
        (_("Rel. pro"), {
            "fields": ("afc", "ipo"),
        }),
        (_("Výdajový filtr"), {
            "fields": (
                "investment", "noninvestment", "remuneration", "personal_costs",
                "education", "consultation", "research", "property", "machines",
                "construction", "administration", "hw", "sw", "lump", "marketing")
        })
    )


admin.site.register(Indicator)
admin.site.register(DotacniTitul, DotacniTitulAdmin)

admin.site.register(Competence)
admin.site.register(Program)
admin.site.register(CallType)

admin.site.register(KodSed)
admin.site.register(OP)
admin.site.register(Field)
admin.site.register(DataSource)
