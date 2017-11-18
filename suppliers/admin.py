from django.contrib import admin

# Register your models here.

from .models import Supplier



class SupplierAdmin(admin.ModelAdmin):

    raw_id_fields = ("address",)
    search_fields = ("name", "regid", "address",)

    fieldsets = [
        ("Identifikace",               {'fields': ['name', "regid", "address"]}),
        ('Kontakt', {'fields': ['phone', "fax", "email", "url"]}),
        ("Zařazení", {"fields": ["sectors", "join_venture", "custom_made",
                        "capital", "turnover", "export", "employes", "year",
                        "main_activity", "certificates"]}),
        ("Osoba", {"fields": ["contact_person"] })
    ]

admin.site.register(Supplier, SupplierAdmin)
