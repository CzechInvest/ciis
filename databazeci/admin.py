from django.contrib import admin
from .models import Contact, Subject, Keyword, Nace, Ket, BusinessArea, Turnover, Employees, Domain, Subdomain, Department, SectorModule, Sector, LegalForm

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "departments", "position",
            "email","voicephone", "companies")

    def companies(self, obj):
        return ", ".join((str(s.name) for s in  Subject.objects.filterc(ontact=obj)))[:15]

    def departments(self, obj):
        return ", ".join(( str(d) for d in obj.department.all()))

class LegalFormAdmin(admin.ModelAdmin):
    list_display = ("form_id", "name")

class SubjectAdmin(admin.ModelAdmin):

    raw_id_fields = ("address", "nace", "legal_form")
    search_fields = ("name", "ico", "legal_form")
    list_filter = ("domain","subdomain", "ket", "nace")
    list_display = ("name", "ico", "contacts", "department", "sectors")
    filter_horizontal = ("domain", "subdomain", "module", "business_area", "contact", "keywords")

    def contacts(self, subj):
        return ", ".join(( str(s) for s in subj.contact.all()))

    def sectors(self, subj):
        return ", ".join(set( str(s.sector) for s in subj.module.all()))

    fieldsets = (
        (None, {
            'fields': ('name', 'ico', 'url', 'department', 'address',
            'legal_form', 'contact',  'keywords', 'domain',
            'subdomain', 'business_area',
            'profile', "product_service", 'note')
        }),
        ('RIN', {
            'fields': ('turnover', 'employees', )
    }),
        ('INO', {
            'fields': ('nace', 'ket')
    }),
        ('SUP', {
            'fields': ('year_founded', 'technology_readiness', "module")
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
admin.site.register(SectorModule)
admin.site.register(Sector)
admin.site.register(Turnover)
admin.site.register(Employees)
admin.site.register(BusinessArea)
admin.site.register(Domain)
admin.site.register(Subdomain)
admin.site.register(Department)
admin.site.register(LegalForm, LegalFormAdmin)
