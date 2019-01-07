from django import forms
from django.forms import ModelForm
from ..models import GreenField
from django.utils.translation import ugettext_lazy as _
from leaflet.forms.widgets import LeafletWidget
from leaflet.forms.fields import PolygonField
from leaflet.forms.fields import PointField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from ..models import Estate
from ..models.media import WasteWater


class PropertyForm(forms.Form):

    class Meta:
        widgets = {'location': LeafletWidget()}

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Fieldset(
                _('Basic info'),
                'property_type',
                'uuid',
                'donation',
                'location',
            ),
            Fieldset(
                _('Contact person'),
                'contact_firstname',
                'contact_lastname',
                'contact_role',
                'contact_phone',
                'contact_mail',
                'contact_language',
                'contact_address',
            ),
            Fieldset(
                _('Owner'),
                'owner_number',
                'owner_type',
                'owner_name',
                'owner_id',
                'owner_phone',
                'owner_mail',
                'owner_language',
            ),
            Fieldset(
                _('Areal properties'),
                'regional_plan',
                'area_description',
                'paracel_numbers',
                'total_area',
                'build_area',
                'free_area',
                'can_devide',
                'smallest_devided_unit',
                'available_since',
                'currency',
                'selling_price_minimal',
                'selling_price_maximal',
                'renting_price_minimal',
                'renting_price_maximal',
                'service_costs',
                'price_note',
            ),
            Fieldset(
                _('Equipment'),
                'agricultural_fund',
                'af_removal_price',
                'previous_usage',
                'hydrogeological_survey',
                'ground_water_level',
                'note',
                'ecological_stress',
                'number_of_levels',
                'heigth',
                'security',
                'fire_protection',
                'heating',
                'air_condition',
                'crane',
                'reception_desk',
                'parking_place',
                'load_lift',
                'personal_lift',
                'canteen',
                'other_equipment',
            ),
            Fieldset(
                _("Media"),
                'electricity_distance',
                'electricity_current',
                'electricity_capacity',
                'electricity_note',
                'drink_water_well',
                'drink_water_distance',
                'drink_water_diameter',
                'drink_water_capacity',
                'drink_water_note',
                'technical_water_well',
                'technical_water_distance',
                'technical_water_diameter',
                'technical_water_capacity',
                'technical_water_note',
                'gas_distance',
                'gas_diameter',
                'gas_pressure',
                'gas_capacity',
                'gas_note',
                'waste_water_type',
                'waste_water_distance',
                'waste_water_diameter',
                'waste_water_capacity',
                'waste_water_technology',
                'waste_water_absorbtion',
                'waste_water_note',

            )
        )

    property_type_choices = (
        ("greenfield", _("Green field")),
        ("development_park", _("Development park")),
        ("industrial_area", _("Industrial area")),
        ("office", _("Office")),
        ("scientific_park", _("Scientific park")),
        ("brownfield", _("Brownfield")),
    )

    uuid = forms.CharField(widget=forms.HiddenInput(), required=False)

    property_type = forms.ChoiceField(
        label=_('Property type'), choices=property_type_choices
    )
    property_name = forms.CharField(label=_('Property name'))
    location = PolygonField(label=_('Location'))
    donation = forms.CharField(label=_('Donation'))

    contact_firstname = forms.CharField(label=_('First name'))
    contact_lastname = forms.CharField(label=_('Last name'))
    contact_role = forms.CharField(label=_('Role'))
    contact_phone = forms.CharField(label=_('Phone'), required=False)
    contact_mail = forms.EmailField(label=_('e-mail'), required=False)
    contact_language = forms.CharField(label=_('Language'), required=False)
    #contact_address = PointField(label=_('Address'))

    owner_type_choices = (
        ("private", _("Private")),
        ("public", _("Public")),
        ("combi", _("Combined")),
    )

    owner_number_choices = (
        (1, _("One")),
        (2, _("Two")),
        (3, _("Many")),
    )

    owner_type = forms.ChoiceField(label=_('Ownership type'), choices=owner_type_choices)
    owner_id = forms.CharField(label=_('ID'), required=False)
    owner_name = forms.CharField(label=_('Name'))
    owner_number = forms.ChoiceField(label=_('Number of owners'),
                                     choices=owner_number_choices)
    owner_phone = forms.CharField(label=_('Phone'), required=False)
    owner_mail = forms.EmailField(label=_('e-mail'), required=False)
    owner_language = forms.CharField(label=_('Language'), required=False)
    # owner_address = forms.EmailField(label=_('Language'))

    regional_plan = forms.CharField(label=_('Regional plan'))
    area_description = forms.CharField(label=_('Area description'),
                                       widget=forms.Textarea,
                                       required=False)
    paracel_numbers = forms.CharField(label=_('Parcel numbers'),
                                      required=False)
    total_area = forms.FloatField(
        label=_('Total area'),
        help_text=_('Total area [m<sup>2</sup>]'))
    build_area = forms.FloatField(
        label=_('Build area'),
        help_text=_('Build area [m<sup>2</sup>]'))
    free_area = forms.FloatField(
        label=_('Free area'),
        help_text=_('Free area [m<sup>2</sup>]'))
    can_devide = forms.BooleanField(
        label=_('Can be devided'))
    smallest_devided_unit = forms.FloatField(
        label=_('Smallest size of division'),
        required=False)
    available_since = forms.DateField(
        label=_('Available since'),
        required=False)

    currency_choices = (
        ("czk", "CZK"),
        ("eur", "EUR"),
    )

    currency = forms.ChoiceField(
        label=_('Label'),
        choices=currency_choices,
        initial="czk")
    selling_price_minimal = forms.FloatField(
        label=_('Minimal selling price'),
        help_text=_('Minimal selling price per m<sup>2</sup>'))
    selling_price_maximal = forms.FloatField(
        label=_('Maximal selling price'),
        help_text=_('Maximal selling price per m<sup>2</sup>'))
    renting_price_minimal = forms.FloatField(
        label=_('Minimal renting price'),
        help_text=_('Minimal renting price per m<sup>2</sup>'))
    renting_price_maximal = forms.FloatField(
        label=_('Maximal renting price'),
        help_text=_('Maximal renting price per m<sup>2</sup>'))
    service_costs = forms.FloatField(
        label=_('Service costs'))
    price_note = forms.CharField(
        label=_('Price note'), widget=forms.Textarea,
        required=False)

    agricultural_fund = forms.BooleanField(
        label=_('Removed from agricultural fund'),
        help_text=_("Taken out of Agriculture fund"))
    af_removal_price = forms.IntegerField(
        label=_('Price for agricultural fund removal'),
        required=False)
    previous_usage = forms.ChoiceField(
        label=_('Previous usage'),
        choices=Estate.previous_usage_choices)
    hydrogeological_survey = forms.BooleanField(
        label=_('Hydrogeological survey'),
        required=False)
    ground_water_level = forms.FloatField(
        label=_('Ground water level'),
        required=False)
    note = forms.CharField(
        label=_('Note'),
        widget=forms.Textarea,
        required=False)
    ecological_stress = forms.ChoiceField(
        label=_('Ecological stress'),
        choices=Estate.ecological_stress_choices,
        required=False)
    number_of_levels = forms.IntegerField(
        label=_('Number of levels'))
    heigth = forms.IntegerField(
        label=_('Height'),
        required=False)

    null_boolean_choices = (
        (None, _("I do not know now")),
        (True, _("Yes I acknowledge this")),
        (False, _("No, I do not like this")),
    )
    security = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=_('Security'),
        initial=None,
        choices=null_boolean_choices)
    fire_protection = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=_('Fire protection'),
        initial=None,
        choices=null_boolean_choices)
    heating = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=_('Heating'),
        initial=None,
        choices=null_boolean_choices)
    air_condition = forms.ChoiceField(
        widget=forms.RadioSelect,
        label=_('Air condition'),
        initial=None,
        choices=null_boolean_choices)
    crane = forms.ChoiceField(
        widget=forms.RadioSelect, label=_('Crane'),
        initial=None,
        choices=null_boolean_choices)
    reception_desk = forms.ChoiceField(
        widget=forms.RadioSelect, label=_('Reception desk'),
        initial=None,
        choices=null_boolean_choices)
    parking_place = forms.ChoiceField(
        widget=forms.RadioSelect, label=_('Parking places'),
        initial=None,
        choices=null_boolean_choices)
    load_lift = forms.ChoiceField(
        widget=forms.RadioSelect, label=_('Load lift'),
        initial=None,
        choices=null_boolean_choices)
    personal_lift = forms.ChoiceField(
        widget=forms.RadioSelect, label=_('Personal lift'),
        initial=None,
        choices=null_boolean_choices)
    canteen = forms.ChoiceField(
        widget=forms.RadioSelect, label=_('Canteen'),
        initial=None,
        choices=null_boolean_choices)
    railway_siding = forms.ChoiceField(
        widget=forms.RadioSelect, label=_('Railway siding'),
        initial=None,
        choices=null_boolean_choices)
    other_equipment = forms.CharField(
        label=_('Other equipment'),
        required=False
    )

    electricity_distance = forms.IntegerField(
        label=_("Electricity distance"))
    electricity_current = forms.IntegerField(
        label=_("Electricity current"),
        required=False)
    electricity_capacity = forms.IntegerField(
        label=_("Electricity capacity"))
    electricity_note = forms.CharField(
        label=_("Electricity note"),
        required=False)

    drink_water_well = forms.BooleanField(
        label=_("Well as drink water source"),
        required=False)
    drink_water_distance = forms.IntegerField(
        label=_("Drink water distance"))
    drink_water_diameter = forms.IntegerField(
        label=_("Drink water diameter"),
        required=False)
    drink_water_capacity = forms.IntegerField(
        label=_("Drink water capacity"),
        required=False)
    drink_water_note = forms.CharField(
        label=_("Drink water note"),
        required=False)

    technical_water_well = forms.BooleanField(
        label=_("Well as technical water source"),
        required=False)
    technical_water_distance = forms.IntegerField(
        label=_("Technical water distance"))
    technical_water_diameter = forms.IntegerField(
        label=_("Technical water diameter"),
        required=False)
    technical_water_capacity = forms.IntegerField(
        label=_("Technical water capacity"),
        required=False)
    technical_water_note = forms.CharField(
        label=_("Technical water note"),
        required=False)

    gas_distance = forms.IntegerField(
        label=_("Gas distance"))
    gas_diameter = forms.IntegerField(
        label=_("Gas diameter"),
        required=False)
    gas_pressure = forms.IntegerField(
        label=_("Gas presure [kPa]"),
        required=False)
    gas_capacity = forms.IntegerField(
        label=_("Gas capacity"),
        required=False)
    gas_note = forms.CharField(
        label=_("Gas note"),
        required=False)

    waste_water_type = forms.ChoiceField(
        label=_("Waste water type"),
        choices=WasteWater.type_choices,
        required=False)
    waste_water_distance = forms.IntegerField(
        label=_("Waste water distnace"))
    waste_water_diameter = forms.IntegerField(
        label=_("Waste water diameter"),
        required=False)
    waste_water_capacity = forms.IntegerField(
        label=_("Waste water capacity"),
        required=False)
    waste_water_technology = forms.CharField(
        label=_("Waste water technology"),
        required=False)
    waste_water_absorbtion = forms.BooleanField(
        label=_("Waste water absorbtion"),
        required=False)
    waste_water_note = forms.CharField(label=_("Waste water note"))


class EstateForm(PropertyForm):
    pass
