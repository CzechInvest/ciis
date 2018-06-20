from django import forms
from .models import Location
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class HighwayPathWidget(forms.Widget):
    template_name = 'highway_path_widget.html'

    class Media:
        js = (
            'js/highway_path_script.js',
        )
        css = {
            'all': (
                'css/highway_path_widget.css',
            )
        }

    def __init__(self, *args, **kwargs):
        super(HighwayPathWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):


        #context = { 'url': "https://router.project-osrm.org/route/v1/driving/{startx},{starty};{destx},{desty}?overview=simplified&geometries=geojson&steps=false".format(startx=start.x, starty=start.y, destx=link.x, desty=link.y)
        #}
        if hasattr(self, "location"):
            start = self.location.geometry.centroid
            link = self.location.get_closest_highway_point().geometry.centroid
            context = {
                    'url': "https://www.openstreetmap.org/directions?engine=ographhopper_car&route={starty},{startx};{destx},{desty}".format(startx=start.x, starty=start.y, destx=link.y, desty=link.x)

            }
        else:
            context = {"empty": True}
        return mark_safe(render_to_string(self.template_name, context))


class LocationForm(forms.ModelForm):

    highway_path = forms.CharField(widget=HighwayPathWidget, required=False)

    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)

        if "instance" in kwargs:
            location = kwargs["instance"]
            self.fields["highway_path"].widget.location = location

