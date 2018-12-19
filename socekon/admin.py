from django.contrib import admin
from .models import Nuts3Stats, Lau1Stats


class Lau1StatsAdmin(admin.ModelAdmin):
    list_display = (
        "lau1",
        "population",
        "work_power",
        "unemployment",
        "unemployment_rate",
        "unemployed_per_job"
    )


class Nuts3StatsAdmin(admin.ModelAdmin):
    list_display = (
        "nuts3",
        "population",
        "work_power",
        "unemployment",
        "unemployment_rate",
        "unemployed_per_job",
        "medium_salary"
    )


admin.site.register(Nuts3Stats, Nuts3StatsAdmin)
admin.site.register(Lau1Stats, Lau1StatsAdmin)
