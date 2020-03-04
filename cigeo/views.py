from django.shortcuts import render
from .models import Nuts3, Lau1
from django.views.generic import ListView
from ciis.views import IndexView as CIISIndexView


class IndexView(CIISIndexView):
    template_name = "cigeo/index.html"


class MapView(ListView):
    template_name = None  # fill this in your class
    model = None  # fill this in your class

    # Providing a useful context_object_name is always a good idea. Your
    # coworkers who design templates will thank you.
    context_object_name = None

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context


class NUTS3View(MapView):
    template_name = "cigeo/nuts3.html"
    model = Nuts3
    context_object_name = "data"


class LAU1View(MapView):
    template_name = "cigeo/lau1.html"
    model = Lau1
    context_object_name = "data"


def index(request):
    context = {
        "user":  request.user
    }
    return render(request, 'cigeo/index.html', context)
