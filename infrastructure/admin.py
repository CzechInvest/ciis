from django.contrib import admin
from .models import Infrastructure

# Register your models here.
class InfrastructureAdmin(admin.ModelAdmin):
    raw_id_fields = ("address",)

    fieldsets = (
        ("Identifikace", {
            "fields": ["name", "inf_type", "short_description", "description",
                "address", "industry", "services",  "year"]}),
        ("On-line resources", {
            "fields": ["url", "facebook", "twitter", "linkedin"]}),
        ("Overview", {
            "fields": ["mentors", "seets", "in_incubation", "conditions",
            "price", "note"]}),
        ("Management", { "fields": ["contact_person"] }),
        ("Partners/Cooperation", { "fields": ["cooperation"] }),
        ("Publication on website", { "fields": ["online_database", "published"] }),
        ("Evaluation", { "fields": ["evaluation"] }),
    )

admin.site.register(Infrastructure, InfrastructureAdmin)
