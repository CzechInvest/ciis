from django.contrib import admin
from .models import Contact, Subject, Keyword, Nace, Ket, Module, Sector, Turnover, Employees, Domain, Subdomain, Department

class ContactAdmin(admin.ModelAdmin):
    pass

class SubjectAdmin(admin.ModelAdmin):

    raw_id_fields = ("address", )
    search_fields = ("name", "ico")
    list_filter = ("domain","subdomain", "module__sector", "ket", "nace")

    fieldsets = (
        (None, {
            'fields': ('name', 'ico', 'url', 'address', 'keywords',
            'department', 'turnover', 'employees', 'contact',
            'profile', 'note')
        }),
        ('Sectors', {
            'fields': ('domain', 'subdomain', 'module', 'ket', 'nace'),
    }),
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Keyword)
admin.site.register(Nace)
admin.site.register(Ket)
admin.site.register(Module)
admin.site.register(Sector)
admin.site.register(Turnover)
admin.site.register(Employees)
admin.site.register(Domain)
admin.site.register(Subdomain)
admin.site.register(Department)
