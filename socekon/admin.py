from django.contrib import admin
from .models import Nuts3Stats, Lau1Stats, HumanResourcesLau1, HumanResourcesNuts3, Date
from cigeo.admin import NUTS3AdminInline, LAU1AdminInline



class Lau1StatsAdmin(admin.ModelAdmin):
    list_display = (
        "lau1",
        "year",
        "population",
        "work_power",
        "unemployment",
        "unemployment_rate",
        "unemployed_per_job"
    )
    search_fields = ("lau1__name",)
    readonly_fields = ("lau1", )
    list_filter = ["lau1", "year"]
    #inlines = (LAU1AdminInline, )


class Nuts3StatsAdmin(admin.ModelAdmin):
    list_display = (
        "nuts3",
        "year",
        "population",
        "work_power",
        "unemployment",
        "unemployment_rate",
        "unemployed_per_job",
        "medium_salary"
    )
    search_fields = ("nuts3__name",)
    readonly_fields = ("nuts3", )
    #inlines = (NUTS3AdminInline, )
    list_filter = ["nuts3", "year"]

class HumanResourcesAdminNuts3(admin.ModelAdmin):

    list_display = (
        "nuts3",
        "inhabitans",
        "productive_inhabitans",
        "unemployed",
        "vacancies",
        "unemployment",
        "applications_per_vacancy",
        "wages",
        "wages_eur",
        "wages_usd",
        "date"
    )


    def wages_eur(self, obj):
        return obj.wages/obj.date.czk_euro

    def wages_usd(self, obj):
        return obj.wages/obj.date.czk_usd


class HumanResourcesAdminLau1(admin.ModelAdmin):

    list_display = (
        "lau1",
        "inhabitans",
        "productive_inhabitans",
        "unemployed",
        "vacancies",
        "unemployment",
        "applications_per_vacancy",
        "date"
    )


admin.site.register(Nuts3Stats, Nuts3StatsAdmin)
admin.site.register(Lau1Stats, Lau1StatsAdmin)

admin.site.register(HumanResourcesNuts3, HumanResourcesAdminNuts3)
admin.site.register(HumanResourcesLau1, HumanResourcesAdminLau1)
admin.site.register(Date)
