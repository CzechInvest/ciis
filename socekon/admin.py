from django.contrib import admin
from django.urls import reverse
import django.urls
from .models import Nuts3Stats, Lau1Stats, HumanResourcesLau1, HumanResourcesNuts3, Date
from cigeo.admin import NUTS3AdminInline, LAU1AdminInline

from django.http import HttpResponseRedirect
from urllib.parse import urlunparse
from urllib.parse import urlencode

def __export_to(modeladmin, request, queryset, frmt):

    selected = queryset.values_list('pk', flat=True)
    args = urlencode({
        "id": ",".join(str(pk) for pk in selected)
        })

    url = urlunparse(
            ["", "",
                reverse('api/socekon/nuts3-list').rstrip("/") + frmt,
                "",
                args,
                ""
             ]
    )

    return HttpResponseRedirect(url)

def export_selected_json(modeladmin, request, queryset):
    return __export_to(modeladmin, request, queryset, ".json")

def export_selected_excel(modeladmin, request, queryset):
    return __export_to(modeladmin, request, queryset, ".xlsx")

export_selected_json.short_description = "Export selected (GeoJSON)"
export_selected_excel.short_description = "Export selected (Excel)"

class HumanResourcesAdminNuts3(admin.ModelAdmin):

    actions = [export_selected_json, export_selected_excel]
    list_filter = ("nuts3", "date")
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

    actions = [export_selected_json, export_selected_excel]
    list_filter = ("lau1", "date")
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


admin.site.register(HumanResourcesNuts3, HumanResourcesAdminNuts3)
admin.site.register(HumanResourcesLau1, HumanResourcesAdminLau1)
admin.site.register(Date)
