from django.contrib import admin
from django.contrib.gis import geos
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
from .models import Lau1
from .models import Nuts3
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
import nested_admin
import json


class LAU1Admin(LeafletGeoAdmin):
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000
    #readonly_fields = ("code", "name",)


class NUTS3Admin(LeafletGeoAdmin):
    default_zoom = 7
    default_lon = 1730000
    default_lat = 6430000

    #readonly_fields = ("code", "name",)


class NUTS3AdminInline(LeafletGeoAdminMixin, admin.StackedInline):
    model = Nuts3


class LAU1AdminInline(LeafletGeoAdminMixin, admin.StackedInline):
    model = Lau1


class NUTS3Filter(admin.SimpleListFilter):
    """Filter for admin interface of NUTS3 regions (Kraje)
    """
    title = _('NUTS3 regions')
    parameter_name = 'nuts3#'

    def lookups(self, request, model_admin):
        nuts3 = Nuts3.objects.all()
        return (
            (obj.id, obj.name) for obj in nuts3
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val:
            nuts3 = Nuts3.objects.get(pk=val)
            results = queryset.filter(
                location__geometry__intersects=nuts3.geometry)
        else:
            results = queryset

        return results


class ArealFieldAdmin(nested_admin.NestedModelAdmin):
    geojson_attributes = []

    def get_place(self, obj):
        if hasattr(obj.location, "address") and \
           obj.location.address is not None:
            return obj.location.address.city
        else:
            return ", ".join(
                [l.__str__() for l in Nuts3.objects.filter(
                    geometry__intersects=obj.location.geometry)])

    def get_search_results(self, request, queryset, search_term):
        """Add NUTS3 (by name) search and area size search (using `<>` operator)
        """

        result, use_distinct = super(
            ArealFieldAdmin, self).get_search_results(
                request, queryset, search_term)
        if search_term:
            if len(result) == 0 or len(result) == len(queryset):
                    result = self._search_lay1_nuts3_by_name(
                        queryset, search_term)
            if len(result) == 0 or len(result) == len(queryset):
                result = self._search_area(queryset, search_term)

        return (result, use_distinct)

    def _search_lay1_nuts3_by_name(self, queryset, search_term):
        """Search NUTS3 (kraje) and LAU1 (okresy) region according to name
        """

        filtered = queryset.none()
        for cls in (Lau1, Nuts3):
            objs = cls.objects.filter(name__startswith=search_term)
            for o in objs:
                objects = queryset.filter(
                    location__geometry__intersects=o.geometry)
                filtered |= objects
        return filtered

    def _search_area(self, queryset, search_term):
        """Search all features, where MIN < area.total < MAX
        """

        filtered = queryset.none()
        if search_term.find("<>") > -1:
            area_min, area_max = [float(x) for x in search_term.split("<>")]
            filtered = queryset.filter(
                    areal__area__total__gte=area_min,
                    areal__area__total__lte=area_max)
        return filtered

    def changelist_view(self, request, extra_context=None):
        """Adjust change list view
        add GeoJSON encoded data for the queryset
        """

        extra_context = extra_context or {}
        response = super().changelist_view(
            request, extra_context=extra_context,
        )
        filtered_query_set = response.context_data["cl"].queryset

        extra_context['objects_data'] = \
            json.dumps(self.as_geojson(filtered_query_set))

        response.context_data.update(extra_context)
        return response

    def as_geojson(self, queryset):
        if self.geojson_attributes:
            attributes = self.geojson_attributes
        else:
            attributes = []

        data = {
            "type": "FeatureCollection",
            "features": []
        }
        for obj in queryset:

            geom = None

            if hasattr(obj, "location_set"):
                multipoint = geos.MultiPoint(
                    [loc.address.coordinates for loc in obj.location_set.all()])
                geom = multipoint.centroid
            elif hasattr(obj, "location"):

                geom = obj.location.geometry.centroid

            if geom:
                title = None
                if hasattr(obj, "title"):
                    title = obj.title
                elif hasattr(obj, "name"):
                    title = obj.name

                feature = {
                    "type": "Feature",
                    "properties": {
                        "name": title,
                        "object_url":
                            reverse('admin:{}_{}_change'.format(
                                obj._meta.app_label,
                                obj._meta.model_name), args=(obj.pk,)),
                    },
                    "geometry": json.loads(geom.json),
                    "id": obj.pk
                }

                size = self.size(obj)
                if size:
                    feature["properties"]["size"] = size

                for attribute in attributes:
                    if hasattr(obj, attribute):
                        feature[attribute] = getattr(obj, attribute.__str__())


                data["features"].append(feature)

        return data


# Register your models here.
admin.site.register(Lau1, LAU1Admin)
admin.site.register(Nuts3, NUTS3Admin)
