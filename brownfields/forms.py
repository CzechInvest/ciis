from django import forms
from django.utils.translation import ugettext_lazy as _
from . models import Brownfield


class BrownfieldForm(forms.Form):
    free_text = forms.CharField(
        label=_('Vyhledávání'), max_length=100)

    location = forms.CharField(
        label=_('Location'), max_length=100)

    location_type = forms.ChoiceField(widget=forms.RadioSelect,
                                      choices=Brownfield.local_type_choices)

    original_usage_type = forms.ChoiceField(widget=forms.RadioSelect,
                                            choices=Brownfield.previous_usage_choices)

    area_min = forms.IntegerField(label=_("Mimimální velikost"))
    area_max = forms.IntegerField(label=_("Maximální velikost"))
