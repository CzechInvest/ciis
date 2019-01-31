from django.contrib import admin
from .models import WhoIsWho
from .models import Institution
from .models import Keyword
from .models import Sector
from .models import WhoIsWho
from .models import ContactPerson
from django.db.models.query import EmptyQuerySet
import re


from leaflet.admin import LeafletGeoAdmin

import nested_admin


class KeywordAdmin(admin.ModelAdmin):
    search_fields = ("kw", )


class SectorAdmin(admin.ModelAdmin):
    search_fields = ("code", "name", )
    list_display = ("code", "name", )


class WhoIsWhoAdmin(admin.ModelAdmin):
    search_fields = ("institution__name", "contact_person__first_name",
                     "contact_person__last_name",
                     "sectors__name", "sectors__code", "keywords__kw",
                     "profile")

    list_display = ("institution", "legal_form", "web", "contact",
                    "sector_codes")

    autocomplete_fields = ("keywords", "sectors")

    list_filter = ("sectors", "institution__legal_form")

    def legal_form(self, wiw):

        return dict(Institution.legal_form_choices)[wiw.institution.legal_form]

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


class ContactPersonInline(nested_admin.NestedStackedInline):
    model = ContactPerson


admin.site.register(WhoIsWho, WhoIsWhoAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
