from django.contrib import admin
from .models import Infrastructure
from .models import Organisation

# Register your models here.
class InfrastructureAdmin(admin.ModelAdmin):
    raw_id_fields = ("address",)

    fieldsets = (
        ("Identifikace", {
            "fields": ["name", "logo", "inf_type", "description_cz", "description_en",
                "address", "industry", "services",  "year"]}),
        ("On-line resources", {
            "fields": ["url", "facebook", "twitter", "linkedin"]}),
        ("Overview", {
            "fields": ["mentors", "seats", "in_incubation", "conditions",
            "price", "note"]}),
        ("Management", { "fields": ["contact_person"] }),
        ("Partners/Cooperation", { "fields": ["cooperation"] }),
    )

admin.site.register(Infrastructure, InfrastructureAdmin)
admin.site.register(Organisation)
