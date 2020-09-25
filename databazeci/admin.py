from django.contrib import admin
from .models import Contact, Subject, Keyword, Nace, Ket, BusinessArea, Turnover, Employees, Domain, Subdomain, Department

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "departments", "position",
            "email","voicephone", "company")

    def company(self, obj):
        return Subject.objects.get(contact=obj)

    def departments(self, obj):
        return ", ".join(( str(d) for d in obj.department.all()))

class SubjectAdmin(admin.ModelAdmin):

    raw_id_fields = ("address", "nace")
    search_fields = ("name", "ico")
    list_filter = ("domain","subdomain", "ket", "nace")
    list_display = ("name", "ico", "contacts", "departments")

    def contacts(self, subj):
        return ", ".join(( str(s) for s in subj.contact.all()))

    def departments(self, subj):
        return ", ".join(( str(d) for d in subj.department.all()))

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
