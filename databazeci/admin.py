from django.contrib import admin
from .models import Contact, Subject, Keyword, Nace, Ket, BusinessArea, Turnover, Employees, Domain, Subdomain, Department, Module, LegalForm, Certificate
from django.utils.translation import gettext_lazy as _
from dynamic_raw_id.admin import DynamicRawIDMixin

class CertificateFilter(admin.SimpleListFilter):
    title = _('Certificates')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'certificate'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """

        data = []
        for o in Certificate.objects.all():
            data.append([o.__str__(), o.pk])

        print(data)
        return data

    def queryset(self, request, queryset):
        if self.value():
            certificate = Certificate.objects.get(pk=int(self.value()))
            return queryset.filter(certificates__in=[certificate])
        else:
            return queryset

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "departments", "position",
            "email","voicephone", "companies")

    def companies(self, obj):
        return ", ".join((str(s.name) for s in  Subject.objects.filterc(ontact=obj)))[:15]

    def departments(self, obj):
        return ", ".join(( str(d) for d in obj.department.all()))

class LegalFormAdmin(admin.ModelAdmin):
    list_display = ("form_id", "name")

class SubjectAdmin(DynamicRawIDMixin, admin.ModelAdmin):


    dynamic_raw_id_fields = ("address", "nace", "legal_form")
    search_fields = ("name", "ico", "legal_form")
    list_filter = ("domain", "subdomain", "ket", "nace", CertificateFilter)
    list_display = ("name", "ico", "contacts", "department")
    filter_horizontal = ("domain", "subdomain", "module", "business_area", "contact", "keywords", "certificates", "ket")

    def contacts(self, subj):
        return ", ".join(( str(s) for s in subj.contact.all()))

    fieldsets = (
        (None, {
            'fields': ('name', 'ico', 'url', 'department', 'address',
            'legal_form', 'contact',  'keywords', 'domain',
            'subdomain', 'business_area',
            'profile', "product_service", 'note')
        }),
        ('RIN', {
            'fields': ('turnover', 'employees',  "certificates")
    }),
        ('INO', {
            'fields': ('nace', 'ket')
    }),
        ('SUP', {
            'fields': ('year_founded', 'technology_readiness', "module",)
    }),
        ('REK', {
            'fields': []
    }),
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Keyword)
admin.site.register(Nace)
admin.site.register(Ket)
admin.site.register(Module)
admin.site.register(Turnover)
admin.site.register(Employees)
admin.site.register(BusinessArea)
admin.site.register(Domain)
admin.site.register(Subdomain)
admin.site.register(Department)
admin.site.register(Certificate)
admin.site.register(LegalForm, LegalFormAdmin)
