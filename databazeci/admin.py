from django.contrib import admin
from .models import Contact, Subject, Keyword, Nace, Ket, BusinessArea, Turnover, Employees, Domain, Subdomain, Department

class ContactAdmin(admin.ModelAdmin):
    pass

class SubjectAdmin(admin.ModelAdmin):

    raw_id_fields = ("address", "nace")
    search_fields = ("name", "ico")
    list_filter = ("domain","subdomain", "ket", "nace")

    fieldsets = (
        (None, {
            'fields': ('name', 'ico', 'url', 'department', 'address',
            'contact',  'keywords', 'domain',
            'subdomain', 'business_area',
            'profile', 'note')
        }),
        ('RIN', {
            'fields': ('turnover', 'employees', )
    }),
        ('INO', {
            'fields': ('nace', 'ket')
    }),
        ('SUP', {
            'fields': ('year_founded', 'technology_readiness')
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
admin.site.register(Turnover)
admin.site.register(Employees)
admin.site.register(BusinessArea)
admin.site.register(Domain)
admin.site.register(Subdomain)
admin.site.register(Department)
