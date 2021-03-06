from django.contrib import admin
from .models import Nuts3Stats, Lau1Stats
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


admin.site.register(Nuts3Stats, Nuts3StatsAdmin)
admin.site.register(Lau1Stats, Lau1StatsAdmin)
