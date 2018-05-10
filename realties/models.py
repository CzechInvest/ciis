from django.db import models
from django.contrib.gis.db import models as gismodels
from cigeo.models import Location
from contacts.models import ContactPerson

class Agent(ContactPerson):
    pass 
    # TODO: fix according to original model

class Owner(ContactPerson):
    pass 
    # TODO: fix according to original model

class Medium(models.Model):
    distance = models.IntegerField(
            help_text="vzdálenost k objektu <code>[m]</code>")

    comment = models.TextField(help_text="Komentář")

class Electricity(Medium):
    current = models.IntegerField(
            help_text="Napětí <code>[kV]</code>")
    capacity = models.IntegerField(
            help_text="Kapacita <code>[kW]</code>")

class Water(Medium):
    diameter = models.IntegerField(
            help_text="Velikost přípojky <code>[mm]</code>")
    well = models.IntegerField(
            help_text="Studna <code>[m<sup>3</sup>]</code>")
    capacity = models.IntegerField(
            help_text="Kapacita přípojky <code>[m<sup>3</sup>/d]</code>")
    well_capacity = models.IntegerField(
            help_text="Kapacita studny <code>[m<sup>3</sup>/d]</code>")

class DrinkingWater(Water):
    pass

class NonPotableWater(Water):
    pass

class Gas(Medium):
    pressure = models.IntegerField(
            help_text="Tlak <code>[kPa]</code>")
    capacity = models.IntegerField(
            help_text="Kapacita přípojky <code>[m<sup>3</sup>/d]</code>")

class WasteWater(Medium):
    diameter = models.IntegerField(
            help_text="Velikost přípojky <code>[mm]</code>")
    capacity = models.IntegerField(
            help_text="Kapacita přípojky <code>[m<sup>3</sup>/d]</code>")

class Telecommunications(Medium):
    pass

class Photo(models.Model):

    title = models.CharField(
        max_length=200,
        help_text="Nadpis fotografie")

    description = models.TextField(
        help_text="Popis fotografie",
        null=True,
        blank=True)

    image = models.ImageField(
        help_text="Soubor s obrázkem"
    )

class Attachment(models.Model):

    title = models.CharField(
        max_length=200,
        help_text="Nadpis dokumentu/přílohy")

    description = models.TextField(
        help_text="Popis dokumentu/přílohy",
        null=True,
        blank=True)

    image = models.FileField(
        help_text="Soubor s dokumentem/přílohou"
    )

class Keyword(models.Model):
    keyword = models.CharField(
            max_length=50,
            blank=False,
            help_text="Klíčové slovo")

class RealEstateType(models.Model):
    title = models.CharField(
            max_length=50
    )
    description = models.CharField(
            max_length=50,
            null=True,
            blank=True
    )

    def __str__(self):
        if self.description:
            return "{} ({})".format(self.title, self.description)
        else:
            return self.title

class OriginalUsage(models.Model):
    usage = models.CharField(
            max_length=50)

class AreaArea(models.Model):

    total = models.IntegerField(
            help_text = "Celková rozloha <code>m<sup>2</sup></code>")
    free = models.IntegerField(
            help_text = "Volná plocha <code>m<sup>2</sup></code>")
    to_be_build = models.IntegerField(
            help_text = "K zástavbě <code>m<sup>2</sup></code>")
    for_expansion = models.IntegerField(
            help_text = "K expanzi <code>m<sup>2</sup></code>")
    available_from = models.DateField(
            help_text = "K dispozici od")
    available_from = models.DateField(
            help_text = "K dispozici od")

class Price(models.Model):
    total_minimum = models.IntegerField(
            help_text="Celková minimální")
    total_maximum = models.IntegerField(
            help_text="Celková maximální")
    per_sqm_minium = models.IntegerField(
            help_text="Za <code>m<sup>2</sup></code> minimální")
    per_sqm_maxium = models.IntegerField(
            help_text="Za <code>m<sup>2</sup></code> maximální")
    note = models.TextField(
            blank=True,
            null=True,
            help_text="Poznámka")

class AreaPrice(models.Model):
    kc = "kc"
    eur = "eur"
    currency_choices = (
            (kc, "Kč"),
            (eur, "Eur"),
    )

    currency = models.CharField(
            max_length=3,
            help_text="Měna",
            choices=currency_choices)

    selling_price = models.OneToOneField(
            Price,
            related_name="selling",
            on_delete=models.CASCADE)

    rental_price = models.OneToOneField(
            Price,
            related_name="rental",
            on_delete=models.CASCADE)

class BuildingPrice(models.Model):
    services_minium = models.IntegerField(
            help_text="Cena za služby minimální")
    services_maxium = models.IntegerField(
            help_text="Cena za služby maximální")
    note = models.TextField(
            blank=True,
            null=True,
            help_text="Poznámka")

class Ownership(models.Model):

    private = 'priv'
    public = 'pub'

    ownership_choices = (
        (private, 'Soukromé'),
        (public, 'Veřejné'),
    )
    ownership = models.CharField(
        max_length=4,
        choices=ownership_choices,
        default=private,
    )

    note = models.TextField(
            help_text = "Poznámka k vlastnictví",
            null=True,
            blank=True
            )

class Purpose(models.Model):


    industry = 'industry'
    storage = 'storage'
    office = 'office'
    purpose_choices = (
        (industry, 'Průmysl'),
        (storage, 'Sklady'),
        (office, 'Kanceláře'),
    )

    purpose = models.CharField(
            max_length=10,
            help_text="Určení dle ÚP",
            choices=purpose_choices,
    )
    purpose_note = models.TextField(
            help_text = "Poznámka k účelu",
            null=True,
            blank=True
            )


class BuildingArea(models.Model):
    production = models.IntegerField(
            default=0,
            help_text="Plocha pro výrobu <code>m<sup>2</sup></code>")
    offices = models.IntegerField(
            default=0,
            help_text="Plocha pro kanceláře <code>m<sup>2</sup></code>")
    storage = models.IntegerField(
            default=0,
            help_text="Plocha pro sklady <code>m<sup>2</sup></code>")
    other = models.IntegerField(
            default=0,
            help_text="Plocha pro jiné užití <code>m<sup>2</sup></code>")

class BuildingDisposal(models.Model):
    floors = models.IntegerField(
            help_text="Počet podlaží",
            null=True,
            blank=True)

    building_type = models.CharField(
            max_length=5,
            help_text="Typ dispozice",
            choices=(("wall", "Příčky"),("os","Open space")),
            null=True, blank=True
    )

    pole_distance = models.FloatField(
            help_text="Rozestup sloupů <code>[m]</code>",
            null=True, blank=True
    )

    loading_capacity = models.FloatField(
            help_text="Nosnost <code>[kg/m<sup>2</sup>]</code>",
            null=True, blank=True
    )

    width = models.FloatField(
            help_text="Šířka <code>[m]</code>",
            blank=True, null=True
    )
    height = models.FloatField(
            help_text="Světlá výška <code>[m]</code>",
            blank=True, null=True
    )
    length = models.FloatField(
            help_text="Délka <code>[m]</code>",
            blank=True, null=True
    )

    input_height = models.FloatField(
            help_text="Výška vstupu <code>[m]</code>",
            blank=True, null=True
    )
    span_width = models.FloatField(
            help_text="Rozpětí nosné konstrukce <code>[m]</code>",
            blank=True, null=True
    )
    construction_material = models.CharField(
            max_length=10,
            help_text="Konstruční materiál",
            blank=True, null=True,
            choices = (
                ("concrete", "Beton"),
                ("brick", "Cihla"),
                ("steel", "Ocel"),
                ("other","Jiná"),
            )
    )

class Floor(models.Model):

    floor_number = models.IntegerField(
            help_text="Číslo podlaží")

    number_of_units = models.IntegerField(
            null=True, blank=True,
            help_text="Počet jednotek")

    total_area = models.IntegerField(
            null=True, blank=True,
            help_text="Celková plocha <code>m<sup>2</sup></code>")

    smallest_unit = models.IntegerField(
            null=True, blank=True,
            help_text="Velikost nejmenší jednotky <code>m<sup>2</sup></code>")

    biggest_unit = models.IntegerField(
            null=True, blank=True,
            help_text="Velikost nevětší jednotky <code>m<sup>2</sup></code>")

    price = models.OneToOneField(BuildingPrice, on_delete=models.CASCADE,
            help_text="Cena")

class Building(models.Model):
    name = models.CharField(
            max_length=50)

    production = "prod"
    administrative = "admin"
    storage = "store"
    multi = "multi"

    building_type_choices = (
        (production, "Výrobní"),
        (administrative, "Administrativní"),
        (storage, "Skladová"),
        (multi, "Multifunkční")
    )

    building_type = models.CharField(
            max_length=5,
            choices=building_type_choices,
            help_text="Typ budovy")

    last_inspection = models.DateField(
            help_text="Datum poslední kolaudace")

    date_available = models.DateField(
            help_text="K dispozici od")


    planed = "planed"
    new = "new"
    reconstructed = "recons"
    good_shape = "good"
    need_reconstruct = "need_rec"
    demolition = "demol"

    technical_state_choices = (
        (planed, "Plánovaný projekt"),
        (new, "Novostavba"),
        (reconstructed, "Rekonstruovaná"),
        (good_shape, "Zachovalá"),
        (need_reconstruct, "Nutná rekonstrukce"),
        (demolition, "K demolici"),
    )

    technical_state = models.CharField(
            max_length=10,
            choices=technical_state_choices,
            help_text="Technický stav budovy")

    ownership = models.OneToOneField(Ownership,
            help_text="Typ vlastnictví",
            on_delete=models.CASCADE)

    last_usage = models.TextField(
            help_text="Poslední využití")
    other_restrictions = models.TextField(
            help_text="Jiná omezení využití")
    total_area = models.OneToOneField(
            BuildingArea,
            related_name="total_area",
            on_delete=models.CASCADE,
            help_text="Celková plocha")
    used_area = models.OneToOneField(
            BuildingArea,
            related_name="used_area",
            on_delete=models.CASCADE,
            help_text="Využitá plocha")
    free_area = models.OneToOneField(
            BuildingArea,
            related_name="free_area",
            on_delete=models.CASCADE,
            help_text="Volná plocha")
    disposal = models.OneToOneField(
            BuildingDisposal,
            related_name="disposal_area",
            on_delete=models.CASCADE,
            help_text="Dispozice")

    price = models.OneToOneField(BuildingPrice, on_delete=models.CASCADE)

    security = models.BooleanField(
            help_text="Bezpečnostní systém")
    fire_protection = models.BooleanField(
            help_text="Protipožární ochrana")
    heating = models.BooleanField(
            help_text="Vytápění")
    air_condition = models.BooleanField(
            help_text="Klimatizace")
    crane = models.BooleanField(
            help_text="Jeřáb")
    reception_desk = models.BooleanField(
            help_text="Recepce")

    parking_garage = models.IntegerField(
            null=True, blank=True,
            help_text="Parkovací místa v garáži")

    parking_openair = models.IntegerField(
            null=True, blank=True,
            help_text="Parkovací místa volně")

    personal_lift_number = models.IntegerField(
            null=True, blank=True,
            help_text="Počet osobních výtahů")

    personal_lift_capacity = models.IntegerField(
            null=True, blank=True,
            help_text="Kapacita osobních výtahů <code>[kg]</code>")

    load_lift_number = models.IntegerField(
            null=True, blank=True,
            help_text="Počet nákladních výtahů")

    load_lift_capacity = models.IntegerField(
            null=True, blank=True,
            help_text="Kapacita nákladních výtahů <code>[kg]</code>")

    menza_capacity = models.IntegerField(
            default=0,
            help_text="Kapacita jídelny")

    notes = models.TextField(
            null=True, blank=True,
            help_text="Poznámky")

    floors = models.ForeignKey(
            Floor,
            on_delete=models.CASCADE,
            help_text="Patra")


class Area(models.Model):
    name = models.CharField(
            max_length=50)

    ownership = models.OneToOneField( Ownership,
        on_delete=models.CASCADE
    )
    purpose = models.OneToOneField( Purpose,
        on_delete=models.CASCADE
    )

    area = models.OneToOneField(AreaArea, on_delete=models.CASCADE)
    price = models.OneToOneField(AreaPrice, on_delete=models.CASCADE)

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
                help_text="Sklon pozemku")

    ground_water = models.IntegerField(
            help_text="Hladina spodní vody <code>m</code>",
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
            help_text="Ekologická zátěž",
            choices=ecology_choices)

    terrain_note = models.TextField(
            null=True,
            blank=True,
            help_text="Poznámka k terénu")

    buildings = models.ManyToManyField(
            Building,
            help_text="Budovy na pozemku")

class RealEstate(models.Model):

    title = models.CharField(
            max_length=200,
            help_text="Název",
            null=False,
            blank=False
    )

    agent = Agent()

    owner = Owner()

    location = models.OneToOneField(
            Location,
            blank=True,
            null=True,
            on_delete=models.CASCADE,
            help_text="Umístění"
    )



    photos = models.ManyToManyField(
            Photo,
            blank=True,
            help_text="Obrázky a fotky"
    )

    documents = models.ManyToManyField(
            Attachment,
            blank=True,
            help_text="Dokumenty a přílohy"
            )

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

    #type = models.ForeignKey(
    #        RealEstateType,
    #        help_text="Typ nemovitosti",
    #        on_delete=models.PROTECT)

    #original_usage = models.ForeignKey(
    #        OriginalUsage,
    #        on_delete=models.PROTECT)

    #date_inserted = models.DateField(
    #    help_text="Datum vložení")

    # contact_person = models.ManyToManyField(ContactPerson)

    #area = models.FloatField(
    #        help_text="Plocha objektu <code>[m<sup>2</sup>]</code>")

    electricity = models.OneToOneField(Electricity, on_delete=models.SET_NULL, help_text="Elektřina", null=True, blank=True)
    drinking_water = models.OneToOneField(DrinkingWater,
            on_delete=models.SET_NULL, help_text="Pitná voda", null=True, blank=True)
    nonpotablewater = models.OneToOneField(NonPotableWater,
            on_delete=models.SET_NULL, help_text="Užitková voda", null=True, blank=True)
    gas = models.OneToOneField(Gas, on_delete=models.SET_NULL, help_text="Plyn", null=True, blank=True)
    waste_water = models.OneToOneField(WasteWater, on_delete=models.SET_NULL, help_text="Odpadní voda", null=True, blank=True)
    telecommunications = models.OneToOneField(Telecommunications,
            on_delete=models.SET_NULL, help_text="Telekomunikace", null=True, blank=True)

    area = models.ForeignKey(
            Area,
            help_text="Plocha",
            on_delete=models.CASCADE)



    def __str__(self):
        return self.title
