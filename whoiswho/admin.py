from django.contrib import admin
from .models import WhoIsWho
from .models import Institution
from .models import Keyword
from .models import Sector
from .models import WhoIsWho
from .models import ContactPerson
from django.http import HttpResponse
from django.db.models.query import EmptyQuerySet
from django.utils.translation import ugettext_lazy as _
import re
from openpyxl import Workbook
import csv
import io
import tempfile
import os
from cigeo.admin import ArealFieldAdmin


from leaflet.admin import LeafletGeoAdmin

def _export(queryset):
    header = [
        "institution", "institution_en", "legal_form", "url", "am", "street",
        "city", "zip", "ICO", "last_name", "first_name", "position", "phone",
        "mail", "specialization", "profile", "keywords", "sector", "notes"
    ]
    data = []
    for whoiswho in queryset:
        if whoiswho.institution.address:
            address = [
                whoiswho.institution.address.adm,
                whoiswho.institution.address.street,
                whoiswho.institution.address.city.name,
                whoiswho.institution.address.zipcode
            ]
        else:
            address =  [None, None, None, None]

        if whoiswho.contact:
            contact = [
                whoiswho.contact_person.first_name,
                whoiswho.contact_person.last_name,
                whoiswho.contact_person.role,
                whoiswho.contact_person.phone,
                whoiswho.contact_person.email
            ]
        else:
            contact = [ None, None, None, None, None ]

        row = [
            whoiswho.institution.name,
            whoiswho.institution.name_en,
            whoiswho.institution.legal_form,
            whoiswho.institution.url] + address + [
            whoiswho.institution.ico
            ] + contact + [
            whoiswho.specialization,
            whoiswho.profile,
            ", ".join([kw.kw for kw in whoiswho.keywords.all()]),
            ",".join([s.code for s in whoiswho.sectors.all()]),
            whoiswho.notes
        ]
        data.append(row)
    return header, data


def export_xlsx(modeladmin, request, queryset):
    file_name = "whoiswho-export.xlsx"
    header, data = _export(queryset)

    wb = Workbook()
    ws = wb["Sheet"]
    header, data = _export(queryset)
    ws.append(header)
    for row in data:
        ws.append(row)

    tmp_file_name = tempfile.mktemp(prefix="ci-whoiswho-export-")
    wb.save(tmp_file_name)

    with open(tmp_file_name, 'rb') as mywb:
        response = HttpResponse(mywb.read())
        response['Content-Disposition'] = \
            'attachment; filename={}'.format(file_name)
        response['Content-Type'] = wb.mime_type
    os.remove(tmp_file_name)

    return response


def export_csv(modeladmin, request, queryset):
    file_name = "whoiswho-export.csv"
    header, data = _export(queryset)

    out = io.StringIO()

    writer = csv.writer(out)
    writer.writerow(header)
    writer.writerows(data)

    out.seek(0)
    response = HttpResponse(out.read())
    response['Content-Disposition'] = \
        'attachment; filename={}'.format(file_name)
    response['Content-Type'] = "text/csv"

    return response


export_csv.short_description = _("Stáhnout jako CSV")
export_xlsx.short_description = _("Stáhnout jako XLSX")

class KeywordAdmin(admin.ModelAdmin):
    search_fields = ("kw", )


class SectorAdmin(admin.ModelAdmin):
    search_fields = ("code", "name", )
    list_display = ("code", "name", )


class WhoIsWhoAdmin(ArealFieldAdmin, LeafletGeoAdmin):
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000
    change_list_template = "admin/change_list-map.html"

    search_fields = ("institution__name", "contact_person__first_name",
                     "contact_person__last_name",
                     "sectors__name", "sectors__code", "keywords__kw",
                     "profile")

    list_display = ("institution", "legal_form", "web", "contact",
                    "sector_codes")

    autocomplete_fields = ("keywords", "sectors")

    list_filter = ("sectors", "institution__legal_form")

    actions = (export_csv, export_xlsx)

    def legal_form(self, wiw):

        if wiw.institution.legal_form:
            return dict(Institution.legal_form_choices)[wiw.institution.legal_form]
        else:
            return 

    def web(self, wiw):
        return wiw.institution.url

    def contact(self, wiw):
        return wiw.contact_person

    def sector_codes(self, wiw):

        return ", ".join([sec.code for sec in wiw.sectors.all()])

    def get_search_results(self, request, queryset, search_term):
        """Custom implementation of search functions
        """

        queryset, use_distinct = super(WhoIsWhoAdmin, self).get_search_results(request, queryset, search_term)
        if re.search(r"AND|NOT|OR", search_term):
            all_objs = WhoIsWho.objects.all()
            if re.search(r"AND", search_term):
                search_term = search_term.replace("AND", "")
                queryset, use_distinct = super(WhoIsWhoAdmin, self).get_search_results(request, queryset, search_term)
            elif re.search(r"OR", search_term):
                first, second = [s.strip() for s in search_term.split("OR")]
                queryset1, use_distinct = super().get_search_results(request, all_objs, first)
                queryset2, use_distinct = super().get_search_results(request, all_objs, second)
                queryset = queryset1.union(queryset2)
            elif re.search(r"NOT", search_term):
                first, second = [s.strip() for s in search_term.split("NOT")]
                queryset1, use_distinct = super().get_search_results(request, all_objs, first)
                queryset2, use_distinct = super().get_search_results(request, all_objs, second)
                queryset = queryset1.difference(queryset2)
        return queryset, use_distinct


class WhoIsWhoInline(admin.TabularInline):
    model = WhoIsWho
    show_change_link = True
    fields = ("institution", ) #, "legal_form", "web", "contact", "sector_codes")
    readonly_fields = ("institution", )


class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ("name", "role", )
    search_fields = ("first_name", "last_name", "role", )
    inlines = (WhoIsWhoInline, )


class InstitutionAdmin(admin.ModelAdmin):

    raw_id_fields = ("address", )

    search_fields = ("name", "legal_form", "ico")

    list_display = ("name", "name_en", "legal_form", "url")

    list_filter = ("legal_form", )


admin.site.register(WhoIsWho, WhoIsWhoAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
