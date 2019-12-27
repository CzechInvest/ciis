from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
import datetime
from django.db.models import Q

# Register your models here.

from .models.matrix import *
from .models.indicators import *

class DotacniTitulStateFilter(admin.SimpleListFilter):
    title = _('State')


    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'date'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            (0, _('Plánováno')),
            (1, _('Vyhlášeno')),
            (2, _('Sběr plná')),
            (3, _('Sběr předběžná')),
            (4, _('Před plnou')),
            (5, _('Ukončeno')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.

        # IF(ISBLANK(P4);(IF(O4>A4;"PLÁNOVÁNO";IF(AND(A4>=O4;A4<R4);"VYHLÁŠENO";IF(AND(A4>=R4;A4<=S4);"SBĚR PLNÁ";IF(AND(A4>Q4;A4<R4);"PŘED PLNOU";IF(A4>S4;"UKONČENO";""))))));(IF(O4>A4;"PLÁNOVÁNO";IF(AND(A4>=O4;A4<P4);"VYHLÁŠENO";IF(AND(A4>=P4;A4<=Q4);"SBĚR PŘEDBĚŽNÁ";IF(AND(A4>=R4;A4<=S4);"SBĚR PLNÁ";IF(AND(A4>Q4;A4<R4);"PŘED PLNOU";IF(A4>S4;"UKONČENO";""))))))))

        #if call > today:
        #        "plánováno"
        #elif today >= call and today < full_from:
        #    "vyhlášeno"
        #elif today >= full_from and today < full_to:
        #    "sběr plná"
        #elif today > call_to and today < full_from:
        #    "před plnou"
        #elif today > full_to:
        #    "ukončeno"
        #elif today >= call and today < call_from:
        #    "vyhlášeno"
        #elif today >= call_from and today <= call_to:
        #    "sběr předběžná"


        today = datetime.date.today()

        value = int(self.value())

        # plánováno
        if value == 0:
            queryset = queryset.filter(date_call__gt=today)

        # vyhlášeno
        elif value == 1:
            queryset = DotacniTitul.objects.filter(
                    Q(date_call__lte=today, date_full_from__gt=today) |
                    Q(date_call__lte=today, date_pref_from__gt=today)
            )

        # sběr plná
        elif value == 2:
            queryset = queryset.filter(date_full_from__lte=today, date_full_to__gt=today)

        # sběr předběžná
        elif value == 3:
            queryset = queryset.filter(date_full_from__lte=today, date_full_to__gt=today)

        # před plnou
        elif value == 4:
            queryset = queryset.filter(date_pref_to__lt=today, date_full_from__gt=today)

        # ukončeno
        elif value == 5:
            queryset = queryset.filter(date_full_to__lt=today)


        return queryset


class DotacniTitulAdmin(admin.ModelAdmin):

    list_display = (
        "name", "changed", "competence", "program", "type", "area", "mp",
        "sp", "vp", "nno", "public", "date_call", "date_pref_from",
        "date_pref_to", "date_full_from", "date_full_to", "allocated", "min",
        "max", "form", "history", "regime", "pkn", "pkv", "url", "afc", "ipo",
        "investment", "noninvestment", "remuneration", "personal_costs",
        "education", "consultation", "research", "property", "machines",
        "construction", "administration", "hw", "sw", "lump", "marketing"
    )

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
        (_("Max. podpor % (o.spol. + NNO)"), {
            "fields": ("mip", "mp", "sp", "vp", "nno", "public"),
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

    list_filter = (DotacniTitulStateFilter,)


class IndicatorAdmin(admin.ModelAdmin):

    list_display = (
        "kod_nci_2014", "npr_envi", "c_s", "fond", "kod_ek", "wf",
        "kod_nci_07_13", "kod_sfc", "unit", "type", "frequency", "resource",
        "resource_comments", "data_source", "es_esf2014", "projects_number"
    )




admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(DotacniTitul, DotacniTitulAdmin)

admin.site.register(Competence)
admin.site.register(Program)
admin.site.register(CallType)

admin.site.register(KodSed)
admin.site.register(OP)
admin.site.register(Field)
admin.site.register(DataSource)
