from django.db import models
from contacts.models import ContactPerson as MyContactPerson
from cigeo.models import Location as MyLocation
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db import models as gis_models


# Create your models here.

class Brownfield(models.Model):

    class Meta:
        verbose_name = _("Brownfield")
        verbose_name_plural = _("Brownfieldy")
        managed = False
        db_table = 'domino\".\"brownfields'

    id = models.IntegerField(
        default=-1,
        primary_key=True
    )
    status = models.IntegerField()
    name = models.CharField(max_length=256)
    geom = gis_models.PointField()
    address = models.TextField()
    description = models.TextField()
    total_area = models.FloatField()
    built_up_area = models.FloatField()
    available_area = models.FloatField()
    is_partible = models.BooleanField()
    available_from = models.DateField()
    currency = models.CharField(max_length=16)
    selling_price_from = models.FloatField()
    selling_price_to = models.FloatField()
    rent_price_from = models.FloatField()
    rent_price_to = models.FloatField()
    access_road = models.TextField()
    telco_kw_medium_distance = models.FloatField()


# class Restriction(models.Model):
# 
#     class Meta:
#         abstract = True
# 
#     applies_choices = (
#         (0, _("Ano")),
#         (1, _("Ne")),
#         (2, _("Neznámé/Neurčené")),
#     )
#     applies = models.IntegerField(
#         verbose_name=_("Vztahuje se na plochu"),
#         choices=applies_choices,
#         default=1)
# 
#     description = models.TextField(
#         blank=True,
#         verbose_name=_("Popis"))
# 
# 
# class EcologicalLimit(Restriction):
# 
#     class Meta:
#         verbose_name = _("Ekologická zátěž")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class ResearchFieldWork(Restriction):
# 
#     class Meta:
#         verbose_name = _("Průzkumné práce")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class CulturalProtection(Restriction):
# 
#     class Meta:
#         verbose_name = _("Ochrana památek")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class GeologicalLimit(Restriction):
# 
#     class Meta:
#         verbose_name = _("Geologické limity")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class NatureConversation(Restriction):
# 
#     class Meta:
#         verbose_name = _("Ochrana přírody")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class WaterConservation(Restriction):
# 
#     class Meta:
#         verbose_name = _("Ochrana podzemních a povrchových vod")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class RoadBuffer(Restriction):
# 
#     class Meta:
#         verbose_name = _("Ochranná pásma komunikací")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class NetworksBuffer(Restriction):
# 
#     class Meta:
#         verbose_name = _("Ochraná pásma inženýrských sítí")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class AgriculturalProtection(Restriction):
# 
#     class Meta:
#         verbose_name = _("Ochraná pásma zemědělského fondu")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class OtherLimits(Restriction):
# 
#     class Meta:
#         verbose_name = _("Jiná omezení")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class EIA(Restriction):
# 
#     class Meta:
#         verbose_name = _("EIA")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class Ownership(models.Model):
# 
#     class Meta:
#         verbose_name = _("Vlastnictví")
#         verbose_name_plural = _("Vlastnictví")
# 
#     private = 'priv'
#     public = 'pub'
# 
#     ownership_choices = (
#         (private, _('Soukromé')),
#         (public, _('Veřejné')),
#     )
#     ownership = models.CharField(
#         max_length=4,
#         verbose_name=_("Vlastnictví"),
#         choices=ownership_choices,
#         default=private,
#     )
# 
#     note = models.TextField(
#         null=True,
#         blank=True,
#         verbose_name=_("Poznámka"),
#         help_text=_("Poznámka"))
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Areal")
#     )
# 
# 
# class Electricity(Medium):
# 
#     class Meta:
#         verbose_name = _("Elektřina")
#         verbose_name_plural = _("Elektřina")
# 
#     current = models.IntegerField(
#         verbose_name=_("Napětí"),
#         help_text=_("Napětí <code>[kV]</code>"))
#     capacity = models.IntegerField(
#         verbose_name=_("Kapacita"),
#         help_text=_("Kapacita <code>[kW]</code>"))
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Brownfield")
#     )
# 
# 
# class DrinkingWater(Water):
# 
#     class Meta:
#         verbose_name = _("Pitná voda")
#         verbose_name_plural = _("Pitná voda")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         related_name="areal",
#         help_text=_("Areal")
#     )
# 
# 
# class NonPotableWater(Water):
# 
#     class Meta:
#         verbose_name = _("Užitková voda")
#         verbose_name_plural = _("Užitková voda")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         related_name="nonpotablewater",
#         on_delete=models.CASCADE,
#         help_text=_("Brownfield")
#     )
# 
# 
# class Gas(Medium):
# 
#     class Meta:
#         verbose_name = _("Plyn")
#         verbose_name_plural = _("Plyn")
# 
#     pressure = models.IntegerField(
#         verbose_name=_("Tlak"),
#         help_text=_("Tlak <code>[kPa]</code>"))
# 
#     capacity = models.IntegerField(
#         verbose_name=_("Kapacita přípojky"),
#         help_text="Kapacita přípojky <code>[m<sup>3</sup>/d]</code>")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Brownfield")
#     )
# 
# 
# class WasteWater(Medium):
# 
#     class Meta:
#         verbose_name = _("Kanalizace")
#         verbose_name_plural = _("Kanalizace")
# 
#     diameter = models.IntegerField(
#         verbose_name=_("Průměr"),
#         help_text="Velikost přípojky <code>[mm]</code>")
# 
#     capacity = models.IntegerField(
#         verbose_name=_("Kapacita přípojky"),
#         help_text="Kapacita přípojky <code>[m<sup>3</sup>/d]</code>")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Brownfield")
#     )
# 
# 
# class Telecommunications(Medium):
# 
#     class Meta:
#         verbose_name = _("Telekomunikace")
#         verbose_name_plural = _("Telekomunikace")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Brownfield")
#     )
# 
# 
# class Location(MyLocation):
# 
#     highway_distance = models.FloatField(
#             default=-1)
# 
#     #airport_distance = models.FloatField(
#     #        default=-1)
# 
#     brownfield = models.OneToOneField(
#         "Brownfield",
#         on_delete=models.CASCADE,
#         help_text="Brownfield"
#     )
# 
# 
# class Road(Medium):
#     class Meta:
#         verbose_name = _("Příjezdová komunikace")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Plocha")
#     )
# 
# 
# class RailRoad(Medium):
# 
#     class Meta:
#         verbose_name = _("Železniční vlečka")
# 
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         help_text=_("Plocha")
#     )
# 
# 
# class Area(AreaArea):
# 
#     areal = models.OneToOneField(
#         "Areal",
#         verbose_name=_('Areál'),
#         on_delete=models.CASCADE)
# 
# 
# class Areal(models.Model):
# 
#     description = models.TextField(
#         blank=True,
#         verbose_name=_("Popis"))
# 
#     status = models.TextField(
#         blank=True,
#         verbose_name=_("Stav areálu"))
# 
#     terrain_adjustment = models.BooleanField(
#         default=False,
#         verbose_name=_("Hrubé terénní úpravy"))
# 
#     slope_choices = (
#         (0, 'Rovina'),
#         (10, 'Mírně svažitý'),
#         (45, 'Svah'),
#     )
#     slope = models.IntegerField(
#         choices=slope_choices,
#         verbose_name=_("Sklon svahu"),
#         help_text=_("Sklon pozemku"))
# 
#     brownfield = models.OneToOneField(
#         "Brownfield",
#         verbose_name=_('Brownfield'),
#         on_delete=models.CASCADE)
# 
# 
# class Brownfield(models.Model):
# 
#     class Meta:
#         verbose_name = _("Brownfield")
#         verbose_name_plural = _("Brownfieldy")
# 
#     title = models.CharField(
#         verbose_name=_("Název"),
#         max_length=200,
#         help_text="Název",
#         blank=False
#     )
# 
#     status_choices = (
#         (0, _("Ke schválení")),
#         (1, _("Rozpracováno")),
#         (2, _("Vráceno k dopracování")),
#         (3, _("Schváleno")),
#         (4, _("Publikováno")),
#     )
#     status = models.IntegerField(
#         verbose_name=_("Stav"),
#         blank=False,
#         choices=status_choices
#     )
# 
#     publish_agreement = models.BooleanField(
#         verbose_name=_("Souhlas s publikací")
#     )
# 
#     contact_details_agreement = models.BooleanField(
#         verbose_name=_("Kontaktní údaje"),
#         help_text=_("Souhlas s poskytnutím kontaktních údajů")
#     )
# 
#     national_program = models.BooleanField(
#         verbose_name=_("Žadatel o dotaci"),
#         help_text=_("Žadatel o dotaci z 'Národního programu'")
#     )
# 
# 
#     local_type_choices = (
#         (0, _("Areál (plocha s budovami)")),
#         (1, _("Objekt (jedna budova)"))
#     )
#     local_type = models.IntegerField(
#         verbose_name=_("Typ lokality"),
#         choices=local_type_choices)
# 
#     location_choices = (
#         (0, _("Pomezí (na okraji zastavěného území obce)")),
#         (1, _("Intravilán (na kraji zastavěného území obce)")),
#         (2, _("Extravilán (mimo zastavěné území obce)"))
#     )
# 
#     location_type = models.IntegerField(
#         verbose_name=_("Poloha lokality"),
#         choices=location_choices)
# 
#     location_characteristics = models.TextField(
#         verbose_name=_("Stručná charakteristika lokality"))
# 
#     build_dat = models.DateField(
#         verbose_name=_("Doba výstavby"))
# 
#     readyness_choices = (
#         (0, _("Lokalita je připravená. Je možná regenerace celé lokality")),
#         (1, _("Lokalita není připravená k procesu regenerace"))
#     )
# 
#     reconstrution_readyness = models.IntegerField(
#         verbose_name=_("Připravenost k rekonstrukci"),
#         choices=readyness_choices)
# 
#     readynes_description = models.TextField(
#         blank=True,
#         verbose_name=_("Popis připravenosti k regeneraci"))
# 
#     previous_usage_choices = (
#         (0, _("Zemědělství")),
#         (1, _("Občanská vybavenost (kulturní domy, služby, obchod, atd.)")),
#         (2, _("Bydlení")),
#         (3, _("Průmysl"))
#     )
# 
#     previous_usage = models.IntegerField(
#         verbose_name=_("Předchozí využití"),
#         choices=previous_usage_choices)
# 
#     previous_usage_description = models.TextField(
#         blank=True,
#         verbose_name=_("Popis předchozího využití"))
# 
#     planed_usage_choices = (
#         (0, _("Zemědělství")),
#         (1, _("Občanská vybavenost (kulturní domy, služby, obchod, atd.)")),
#         (2, _("Bydlení")),
#         (3, _("Průmysl a podnikání (služby a kanceláře)")),
#         (4, _("Průmsl, monofunkce"))
#     )
# 
#     planed_usage = models.IntegerField(
#         verbose_name=_("Plánované využití"),
#         choices=planed_usage_choices)
# 
#     planed_usage_description = models.TextField(
#         blank=True,
#         verbose_name=_("Popis plánovaného využití"))
# 
#     upd_choices = (
#         (0, _("Zemědělství, výrba")),
#         (1, _("Smíšená zástavba")),
#         (2, _("Smíšená zóna")),
#         (3, _("Plochy smíšené výrobní")),
#     )
# 
#     upd = models.IntegerField(
#         verbose_name=_("Územě plánovací dokumantace (ÚPD)"),
#         choices=upd_choices)
# 
#     upd_conflict = models.TextField(
#         blank=True,
#         verbose_name=_("Možný střet navrhovaného využití s ÚPD"))
# 
#     upd_note = models.TextField(
#         blank=True,
#         verbose_name=_("Poznámka k ÚPD"))
# 
#     local_government_support = models.BooleanField(
#         default=True,
#         verbose_name=_("Podpora regenerace místní samosprávou"))
# 
#     local_government_support_description = models.TextField(
#         blank=True,
#         verbose_name=_("Popis podpory"))
# 
#     previous_support_choices = (
#         (0, _("Žádná")),
#         (1, _("Využití dotací")),
#         (2, _("..."))
#     )
#     previous_support_type = models.IntegerField(
#         default=0,
#         choices=previous_support_choices,
#         verbose_name=_("Dřívější podpora z veřejných zdrojů"))
# 
#     @property
#     def json(self):
#         return {
#             "title": self.title,
#             "id": self.id,
#             "location": self.location.json
#         }
# 
#     def __str__(self):
#         return self.title
# 
# 
# class Photo(models.Model):
# 
#     class Meta:
#         verbose_name = _("Fotografie")
#         verbose_name_plural = _("Fotografie")
# 
#     title = models.CharField(
#         verbose_name=_("Název"),
#         max_length=200,
#         help_text="Nadpis fotografie")
# 
#     description = models.TextField(
#         verbose_name=_("Popis"),
#         help_text="Popis fotografie",
#         null=True,
#         blank=True)
# 
#     image = models.ImageField(
#         verbose_name=_("Obrázek"),
#         help_text="Soubor s obrázkem"
#     )
# 
#     brownfield = models.ForeignKey(
#         "Brownfield",
#         verbose_name=_("Brownfield"),
#         on_delete=models.CASCADE,
#         help_text="Brownfield"
#     )
# 
#     def __str__(self):
#         return self.title
# 
# 
# class Attachment(models.Model):
# 
#     class Meta:
#         verbose_name = _("Přílohy")
#         verbose_name_plural = _("Přílohy")
# 
#     title = models.CharField(
#         verbose_name=_("Název"),
#         max_length=200,
#         help_text=_("Nadpis dokumentu/přílohy"))
# 
#     description = models.TextField(
#         verbose_name=_("Popis"),
#         help_text=_("Popis dokumentu/přílohy"),
#         null=True,
#         blank=True)
# 
#     attachment = models.FileField(
#         verbose_name=_("Příloha"),
#         help_text=_("Soubor s dokumentem/přílohou")
#     )
# 
#     brownfield = models.ForeignKey(
#         "Brownfield",
#         verbose_name=_("Brownfield"),
#         on_delete=models.CASCADE,
#         help_text=_("Brownfield")
#     )
# 
# 
# class Keeper(MyContactPerson):
#     areal = models.OneToOneField(
#         "Areal",
#         on_delete=models.CASCADE,
#         verbose_name=_("Brownfield"),
#         help_text="Brownfield")
