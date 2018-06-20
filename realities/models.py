from django.db import models
from cigeo.models import Location as MyLocation
from contacts.models import ContactPerson as MyContactPerson
from django.utils.translation import ugettext_lazy as _
from cigeo.models import Area as MyAreaArea
from cigeo.models import Water
from cigeo.models import Medium


class ContactPerson(MyContactPerson):
    pass


class Location(MyLocation):

    help_text = _("Vzdálenost k dálnici")

    highway_distance = models.FloatField(
            default=-1,
            help_text=help_text)
    real_estate = models.OneToOneField(
            "RealEstate",
            on_delete=models.CASCADE,
            help_text="Nemovitost"
    )


class Agent(ContactPerson):
    class Meta:
        verbose_name = _("Agent")
        verbose_name_plural = _("Agenti")

    # TODO: fix according to original model

class Owner(ContactPerson):
    class Meta:
        verbose_name = _("Vlastník")
        verbose_name_plural = _("Vlastníci")

    # TODO: fix according to original model

class Electricity(Medium):

    class Meta:
        verbose_name = _("Elektřina")
        verbose_name_plural = _("Elektřina")

    current = models.IntegerField(
            verbose_name=_("Napětí"),
            help_text=_("Napětí <code>[kV]</code>"))
    capacity = models.IntegerField(
            verbose_name=_("Kapacita"),
            help_text=_("Kapacita <code>[kW]</code>"))

    real_estate = models.OneToOneField(
            "RealEstate",
            on_delete=models.CASCADE,
            help_text=_("Nemovitost")
    )


class DrinkingWater(Water):

    class Meta:
        verbose_name = _("Pitná voda")
        verbose_name_plural = _("Pitná voda")

    real_estate = models.OneToOneField(
            "RealEstate",
            verbose_name=_("Nemovitost"),
            related_name="real_estate",
            on_delete=models.CASCADE,
            help_text=_("Nemovitost")
    )


class NonPotableWater(Water):

    class Meta:
        verbose_name = _("Užitková voda")
        verbose_name_plural = _("Užitková voda")

    real_estate = models.OneToOneField(
            "RealEstate",
            on_delete=models.CASCADE,
            help_text=_("Nemovitost")
    )

class Gas(Medium):

    class Meta:
        verbose_name = _("Plyn")
        verbose_name_plural = _("Plyn")

    pressure = models.IntegerField(
            verbose_name=_("Tlak"),
            help_text=_("Tlak <code>[kPa]</code>"))

    capacity = models.IntegerField(
            verbose_name=_("Kapacita přípojky"),
            help_text="Kapacita přípojky <code>[m<sup>3</sup>/d]</code>")

    real_estate = models.OneToOneField(
            "RealEstate",
            on_delete=models.CASCADE,
            help_text="Nemovitost"
    )

class WasteWater(Medium):

    class Meta:
        verbose_name = _("Kanalizace")
        verbose_name_plural = _("Kanalizace")

    diameter = models.IntegerField(
            verbose_name=_("Průměr"),
            help_text="Velikost přípojky <code>[mm]</code>")

    capacity = models.IntegerField(
            verbose_name=_("Kapacita přípojky"),
            help_text="Kapacita přípojky <code>[m<sup>3</sup>/d]</code>")

    real_estate = models.OneToOneField(
            "RealEstate",
            verbose_name=_("Nemovitost"),
            on_delete=models.CASCADE,
            help_text=_("Nemovitost")
    )

class Telecommunications(Medium):

    class Meta:
        verbose_name = _("Telekomunikace")
        verbose_name_plural = _("Telekomunikace")

    real_estate = models.OneToOneField(
            "RealEstate",
            blank=True,
            null=True,
            on_delete=models.CASCADE,
            help_text="Nemovitost"
    )

class Photo(models.Model):

    class Meta:
        verbose_name = _("Fotografie")
        verbose_name_plural = _("Fotografie")

    title = models.CharField(
        verbose_name=_("Název"),
        max_length=200,
        help_text="Nadpis fotografie")


    description = models.TextField(
        verbose_name=_("Popis"),
        help_text="Popis fotografie",
        null=True,
        blank=True)

    image = models.ImageField(
        verbose_name=_("Obrázek"),
        help_text="Soubor s obrázkem"
    )

    real_estate = models.ForeignKey(
            "RealEstate",
            verbose_name=_("Nemovitost"),
            on_delete=models.CASCADE,
            help_text="Nemovitost"
    )

class Attachment(models.Model):

    class Meta:
        verbose_name = _("Přílohy")
        verbose_name_plural = _("Přílohy")

    title = models.CharField(
        verbose_name=_("Název"),
        max_length=200,
        help_text=_("Nadpis dokumentu/přílohy"))

    description = models.TextField(
        verbose_name=_("Popis"),
        help_text=_("Popis dokumentu/přílohy"),
        null=True,
        blank=True)

    attachment = models.FileField(
        verbose_name=_("Příloha"),
        help_text=_("Soubor s dokumentem/přílohou")
    )

    real_estate = models.ForeignKey(
            "RealEstate",
            verbose_name=_("Nemovitost"),
            on_delete=models.CASCADE,
            help_text=_("Nemovitost")
    )

class Keyword(models.Model):
    keyword = models.CharField(
            max_length=50,
            blank=False,
            help_text="Klíčové slovo")

class OriginalUsage(models.Model):
    usage = models.CharField(
            max_length=50)

class AreaArea(MyAreaArea):


    area = models.OneToOneField(
            "Area",
            verbose_name=_('Plocha'),
            on_delete=models.CASCADE)


class Price(models.Model):

    total_minimum = models.IntegerField(
            verbose_name=_("Celková minimální"),
            help_text=_("Celková minimální"))
    total_maximum = models.IntegerField(
            verbose_name=_("Celková maximální"),
            help_text=_("Celková maximální"))
    per_sqm_minium = models.IntegerField(
            verbose_name=_("Za m minimální"),
            help_text=_("Za <code>m<sup>2</sup></code> minimální"))
    per_sqm_maxium = models.IntegerField(
            verbose_name=_("Za m maximální"),
            help_text=_("Za <code>m<sup>2</sup></code> maximální"))
    note = models.TextField(
            blank=True,
            null=True,
            verbose_name=_("Poznámka"),
            help_text=_("Poznámka"))

class SellingPrice(Price):

    class Meta:
        verbose_name = _("Prodejní cena")
        verbose_name_plural = _("Prodejní ceny")

    area = models.OneToOneField(
            "AreaPrice",
            on_delete=models.CASCADE)

class RentalPrice(Price):

    class Meta:
        verbose_name = _("Nájemní cena")
        verbose_name_plural = _("Nájemní ceny")

    area = models.OneToOneField(
            "AreaPrice",
            on_delete=models.CASCADE)


class AreaPrice(models.Model):

    class Meta:
        verbose_name = _("Cena")
        verbose_name_plural = _("Ceny")

    kc = "kc"
    eur = "eur"
    currency_choices = (
            (kc, "Kč"),
            (eur, "Eur"),
    )

    currency = models.CharField(
            max_length=3,
            verbose_name=_("Měna"),
            help_text=_("Měna"),
            choices=currency_choices)

    area = models.OneToOneField(
            "Area",
            on_delete=models.CASCADE)

class BuildingPrice(models.Model):

    class Meta:
        verbose_name = _("Cena budovy")
        verbose_name_plural = _("Ceny bodvy")

    services_minium = models.IntegerField(
            verbose_name=_("Minimální cena za služby"),
            help_text=_("Cena za služby minimální"))
    services_maxium = models.IntegerField(
            verbose_name=_("Maximální cena za služby"),
            help_text=_("Cena za služby maximální"))
    note = models.TextField(
            blank=True,
            null=True,
            verbose_name=_("Poznámka"),
            help_text=_("Poznámka"))

    building = models.OneToOneField(
            "building",
            on_delete=models.CASCADE)

class Ownership(models.Model):

    class Meta:
        verbose_name = _("Vlastnictví")
        verbose_name_plural = _("Vlastnictví")

    private = 'priv'
    public = 'pub'

    ownership_choices = (
        (private, _('Soukromé')),
        (public, _('Veřejné')),
    )
    ownership = models.CharField(
        max_length=4,
        verbose_name=_("Vlastnictví"),
        choices=ownership_choices,
        default=private,
    )

    note = models.TextField(
            null=True,
            blank=True,
            verbose_name=_("Poznámka"),
            help_text=_("Poznámka"))


class BuildingOwnership(Ownership):

    class Meta:
        verbose_name = _("Vlastnictví budovy")
        verbose_name_plural = _("Vlastnictví budovy")

    building = models.OneToOneField(
        "Building",
        on_delete=models.CASCADE
    )

class AreaOwnership(Ownership):

    class Meta:
        verbose_name = _("Vlastnictví plochy")
        verbose_name_plural = _("Vlastnictví plochy")

    area = models.OneToOneField(
        "Area",
        on_delete=models.CASCADE
    )

class Purpose(models.Model):

    class Meta:
        verbose_name = _("Účel")
        verbose_name_plural = _("Účely")

    industry = 'industry'
    storage = 'storage'
    office = 'office'
    purpose_choices = (
        (industry, _('Průmysl')),
        (storage, _('Sklady')),
        (office, _('Kanceláře')),
    )

    purpose = models.CharField(
            max_length=10,
            verbose_name=_("Určení"),
            help_text=_("Určení dle ÚP"),
            choices=purpose_choices,
    )
    note = models.TextField(
            verbose_name = _("Poznámka"),
            help_text = _("Poznámka"),
            null=True,
            blank=True
            )

    area = models.OneToOneField(
        "Area",
        on_delete=models.CASCADE
    )

class BuildingArea(models.Model):

    class Meta:
        verbose_name = _("Plocha budovy")
        verbose_name_plural = _("Plochy budovy")

    production = models.IntegerField(
            default=0,
            verbose_name=_("Plocha pro výrobu"),
            help_text=_("Plocha pro výrobu <code>m<sup>2</sup></code>"))
    offices = models.IntegerField(
            default=0,
            verbose_name=_("Plocha kancláře"),
            help_text=_("Plocha pro kanceláře <code>m<sup>2</sup></code>"))
    storage = models.IntegerField(
            default=0,
            verbose_name=_("Plocha sklady"),
            help_text=_("Plocha pro sklady <code>m<sup>2</sup></code>"))
    other = models.IntegerField(
            default=0,
            verbose_name=_("Plocha pro jiné využité"),
            help_text=_("Plocha pro jiné užití <code>m<sup>2</sup></code>"))

class TotalBuildingArea(BuildingArea):
    class Meta:
        verbose_name = _("Celková plocha budovy")
        verbose_name_plural = _("Celkové plochy budovy")

class UsedBuildingArea(BuildingArea):
    class Meta:
        verbose_name = _("Využitá plocha budovy")
        verbose_name_plural = _("Využité plochy budovy")

class FreeBuildingArea(BuildingArea):
    class Meta:
        verbose_name = _("Volné plochy budovy")
        verbose_name_plural = _("Volné plochy budovy")

class BuildingDisposal(models.Model):

    class Meta:
        verbose_name = _("Propozice budovy")
        verbose_name_plural = _("Propozice budovy")

    floors = models.IntegerField(
            verbose_name=_("Počet podlaží"),
            help_text=_("Počet podlaží"),
            null=True,
            blank=True)

    building_type = models.CharField(
            max_length=5,
            verbose_name=_("Typ dispozice"),
            help_text=_("Typ dispozice"),
            choices=(("wall", _("Příčky")),("os",_("Open space"))),
            null=True, blank=True
    )

    pole_distance = models.FloatField(
            verbose_name=_("Rozestup sloupů"),
            help_text=_("Rozestup sloupů <code>[m]</code>"),
            null=True, blank=True
    )

    loading_capacity = models.FloatField(
            verbose_name=_("Nosnost"),
            help_text=_("Nosnost <code>[kg/m<sup>2</sup>]</code>"),
            null=True, blank=True
    )

    width = models.FloatField(
            verbose_name=_("Šířka"),
            help_text=_("Šířka <code>[m]</code>"),
            blank=True, null=True
    )
    height = models.FloatField(
            verbose_name=_("Světlá výška"),
            help_text=_("Světlá výška <code>[m]</code>"),
            blank=True, null=True
    )
    length = models.FloatField(
            verbose_name=_("Délka"),
            help_text=_("Délka <code>[m]</code>"),
            blank=True, null=True
    )

    input_height = models.FloatField(
            verbose_name=_("Výška vstupu"),
            help_text=_("Výška vstupu <code>[m]</code>"),
            blank=True, null=True
    )
    span_width = models.FloatField(
            verbose_name=_("Rozpětí konstrukce"),
            help_text=_("Rozpětí nosné konstrukce <code>[m]</code>"),
            blank=True, null=True
    )
    construction_material = models.CharField(
            max_length=10,
            verbose_name=_("Konstruční materiál"),
            help_text=_("Konstruční materiál"),
            blank=True, null=True,
            choices = (
                ("concrete", _("Beton")),
                ("brick", _("Cihla")),
                ("steel", _("Ocel")),
                ("other",_("Jiná")),
            )
    )

    building = models.OneToOneField(
            "Building",
            on_delete=models.CASCADE)

class Floor(models.Model):

    class Meta:
        verbose_name = _("Patro")
        verbose_name_plural = _("Patra")

    floor_number = models.IntegerField(
            verbose_name=_("Podlaží"),
            help_text=_("Číslo podlaží"))

    number_of_units = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Počet jednotek"),
            help_text=_("Počet jednotek"))

    total_area = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Celková plocha"),
            help_text=_("Celková plocha <code>m<sup>2</sup></code>"))

    smallest_unit = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Plocha nejmenší jednotky"),
            help_text=_("Velikost nejmenší jednotky <code>m<sup>2</sup></code>"))

    biggest_unit = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Plocha největší jednotky"),
            help_text=_("Velikost nevětší jednotky <code>m<sup>2</sup></code>"))

    building = models.ForeignKey(
            "Building",
            verbose_name=_("Budova"),
            on_delete=models.CASCADE,
            help_text=_("Budova"))



class Building(models.Model):

    class Meta:
        verbose_name = _("Budova")
        verbose_name_plural = _("Budova")

    class Meta:
        verbose_name = _("Budova")
        verbose_name_plural = _("Budovy")

    name = models.CharField(
            verbose_name=_("Název"),
            max_length=50)

    production = "prod"
    administrative = "admin"
    storage = "store"
    multi = "multi"

    building_type_choices = (
        (production, _("Výrobní")),
        (administrative, _("Administrativní")),
        (storage, _("Skladová")),
        (multi, _("Multifunkční"))
    )

    building_type = models.CharField(
            max_length=5,
            choices=building_type_choices,
            verbose_name=_("Typ budovy"),
            help_text=_("Typ budovy"))

    last_inspection = models.DateField(
            verbose_name=_("Poslední kolaudace"),
            help_text=_("Datum poslední kolaudace"))

    date_available = models.DateField(
            verbose_name=_("K dispozici od"),
            help_text=_("K dispozici od"))


    planed = "planed"
    new = "new"
    reconstructed = "recons"
    good_shape = "good"
    need_reconstruct = "need_rec"
    demolition = "demol"

    technical_state_choices = (
        (planed, _("Plánovaný projekt")),
        (new, _("Novostavba")),
        (reconstructed, _("Rekonstruovaná")),
        (good_shape, _("Zachovalá")),
        (need_reconstruct, _("Nutná rekonstrukce")),
        (demolition, _("K demolici")),
    )

    technical_state = models.CharField(
            max_length=10,
            choices=technical_state_choices,
            verbose_name=_("Technický stav"),
            help_text=_("Technický stav budovy"))


    last_usage = models.TextField(
            verbose_name=_("Poslední využití"),
            help_text=_("Poslední využití"))
    other_restrictions = models.TextField(
            verbose_name=_("Jiná omezení"),
            help_text=_("Jiná omezení využití"))


    security = models.BooleanField(
            verbose_name=_("Bezpečnostní systém"),
            help_text=_("Bezpečnostní systém"))

    fire_protection = models.BooleanField(
            verbose_name=_("Protipožární ochrana"),
            help_text=_("Protipožární ochrana"))

    heating = models.BooleanField(
            verbose_name=_("Vytápění"),
            help_text=_("Vytápění"))

    air_condition = models.BooleanField(
            verbose_name=_("Klimatizace"),
            help_text=_("Klimatizace"))

    crane = models.BooleanField(
            verbose_name=_("Jeřáb"),
            help_text=_("Jeřáb"))

    reception_desk = models.BooleanField(
            verbose_name=_("Recepce"),
            help_text=_("Recepce"))

    parking_garage = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Parkovací místa v garáži"),
            help_text=_("Parkovací místa v garáži"
            ))

    parking_openair = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Parkovací místa volně"),
            help_text=_("Parkovací místa volně"))

    personal_lift_number = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Počet osobních výtahů"),
            help_text=_("Počet osobních výtahů"))

    personal_lift_capacity = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Kapacita osobních výtahů"),
            help_text=_("Kapacita osobních výtahů <code>[kg]</code>"))

    load_lift_number = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Počet nákladních výtahů"),
            help_text=_("Počet nákladních výtahů"))

    load_lift_capacity = models.IntegerField(
            null=True, blank=True,
            verbose_name=_("Kapacita nákladních výtahů"),
            help_text=_("Kapacita nákladních výtahů <code>[kg]</code>"))

    menza_capacity = models.IntegerField(
            default=None,
            null=True,
            blank=True,
            verbose_name=_("Kapacita jídelny"),
            help_text=_("Kapacita jídelny"))

    notes = models.TextField(
            null=True, blank=True,
            verbose_name=_("Poznámky"),
            help_text=_("Poznámky"))


    area = models.ForeignKey(
            "Area",
            on_delete=models.CASCADE,
            verbose_name=_("Plocha"),
            help_text=_("Plocha"))


class Area(models.Model):

    class Meta:
        verbose_name = _("Plocha")
        verbose_name_plural = _("Plochy")

    name = models.CharField(
            verbose_name=_("Název"),
            max_length=50)

    plain = 0
    semi_slope = 10
    slope = 45

    slope_choices = (
        (plain, 'Rovina'),
        (semi_slope, 'Mírně svažitý'),
        (slope, 'Svah'),
    )
    slope = models.IntegerField(
                choices=slope_choices,
                verbose_name=_("Sklon svahu"),
                help_text=_("Sklon pozemku"))

    ground_water = models.IntegerField(
            verbose_name=_("Spodní voda"),
            help_text=_("Hladina spodní vody <code>m</code>"),
            null=True,
            blank=True)

    no = 0
    yes = 1
    canbe = 2
    unknown = 3

    ecology_choices = (
        (no, 'Ne'),
        (yes, 'Ano'),
        (canbe, 'Lze předpokládat'),
        (unknown, 'Neznámé'),
    )

    ecology = models.IntegerField(
            verbose_name=_("Ekologická zátěž"),
            help_text=_("Ekologická zátěž"),
            choices=ecology_choices)

    note = models.TextField(
            null=True,
            blank=True,
            verbose_name=_("Poznámka"),
            help_text=_("Poznámka k terénu"))


    real_estate = models.OneToOneField(
            "RealEstate",
            on_delete=models.CASCADE,
            help_text="Nemovitost"
    )


class RealEstate(models.Model):

    class Meta:
        verbose_name = _("Nemovitost")
        verbose_name_plural = _("Nemovitosti")

    title = models.CharField(
            verbose_name=_("Název"),
            max_length=200,
            help_text="Název",
            null=False,
            blank=False
    )

    agent = models.ForeignKey(Agent,
        on_delete=models.SET_NULL,
        verbose_name=_("Agent"),
        null=True,
        help_text="Agent")

    owner = models.ForeignKey(Owner,
        on_delete=models.SET_NULL,
        verbose_name=_("Vlastník"),
        null=True,
        help_text="Vlastník")


    #description = models.TextField(
    #        help_text="Popis",
    #        blank=True,
    #        null=True
    #)

    #keywords = models.ManyToManyField(
    #        Keyword,
    #        blank=True,
    #        help_text="Klíčová slova"
    #)

    type_choices = (
        (0, _("Greenfield/Průmyslová zóna")),
        (1, _("Průmyslový park")),
        (2, _("areál")),
        (3, _("Vědecko-technický park")),
        (4, _("Kanceláře")),
    )

    realestate_type = models.IntegerField(
            choices=type_choices,
            help_text="Typ nemovitosti",
        )

    #original_usage = models.ForeignKey(
    #        OriginalUsage,
    #        on_delete=models.PROTECT)

    #date_inserted = models.DateField(
    #    help_text="Datum vložení")

    # contact_person = models.ManyToManyField(ContactPerson)

    #area = models.FloatField(
    #        help_text="Plocha objektu <code>[m<sup>2</sup>]</code>")




    def __str__(self):
        return self.title
