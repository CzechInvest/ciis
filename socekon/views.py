from cigeo.views import MapView
from .models import HumanResourcesNuts3, HumanResourcesLau1
from ciis.views import IndexView as CIISIndexView


class IndexView(CIISIndexView):
    template_name = "socekon/index.html"


class MapViewNuts3(MapView):
    model = HumanResourcesNuts3
    context_object_name = "data"


class MapViewLau1(MapView):
    model = HumanResourcesLau1
    context_object_name = "data"
