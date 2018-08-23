from django import forms
from .models.generic import Location
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class PathWidget(forms.Widget):
    template_name = 'path_widget.html'

    class Media:
        js = (
            'js/path_script.js',
        )
        css = {
            'all': (
                'css/path_widget.css',
            )
        }

    def __init__(self, *args, **kwargs):
        super(PathWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):

        # context = { 'url': "https://router.project-osrm.org/route/v1/" +
        #                   "driving/{startx},{starty};{destx},{desty}?" +
        #                   "overview=simplified&geometries=geojson&" +
        #                   "steps=false".format(startx=start.x,
        #                                               starty=start.y,
        #                                               destx=link.x,
        #                                               desty=link.y)
        #           }

        if hasattr(self, "location"):
            start = self.location.geometry.centroid
            link = self.location.get_closest_point(self.to).geometry.centroid
            context = {
                'url': "https://www.openstreetmap.org/directions?engine="
                       "ographhopper_car&route={starty},{startx};"
                       "{destx},{desty}".format(startx=start.x, starty=start.y,
                                                destx=link.y, desty=link.x),
                'distance': getattr(self.location, self.to+'_distance')

            }
        else:
            context = {"empty": True}
        return mark_safe(render_to_string(self.template_name, context))


class HighwayPathWidget(PathWidget):
    to = "highway"


class AirportPathWidget(PathWidget):
    to = "airport"


class RailwayPathWidget(PathWidget):
    to = "railway"


class PublicTransportPathWidget(PathWidget):
    to = "public_transport"


class LocationForm(forms.ModelForm):

    highway_distance = forms.CharField(widget=HighwayPathWidget,
                                       required=False)
    airport_distance = forms.CharField(widget=AirportPathWidget,
                                       required=False)
    railway_distance = forms.CharField(widget=RailwayPathWidget,
                                       required=False)
    public_transport_distance = forms.CharField(
        widget=PublicTransportPathWidget, required=False)

    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)

        if "instance" in kwargs:
            location = kwargs["instance"]
            self.fields["highway_distance"].widget.location = location
            self.fields["railway_distance"].widget.location = location
            self.fields["airport_distance"].widget.location = location
            self.fields["public_transport_distance"].widget.location = location
