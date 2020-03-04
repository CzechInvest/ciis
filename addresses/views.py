from .models import Address
from django.views.generic import ListView


class AddressView(ListView):
    template_name = "addresses/address_list.html"
    model = Address
    context_object_name = "data"
    paginate_by = 100
