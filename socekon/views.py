from cigeo.views import MapView
from .models import Nuts3Stats, Lau1Stats
from ciis.views import IndexView as CIISIndexView


class IndexView(CIISIndexView):
    template_name = "socekon/index.html"


class MapViewNuts3(MapView):
    model = Nuts3Stats
    context_object_name = "data"


class MapViewLau1(MapView):
    model = Lau1Stats
    context_object_name = "data"
