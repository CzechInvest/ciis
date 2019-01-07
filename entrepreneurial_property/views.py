from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EstateForm
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *

ALL_TYPES = [Brownfield, GreenField, DevelopmentPark, IndustrialAreal, Office,
             ScientificPark]


def public_estates(request):
    form = EstateForm()

    return HttpResponse("All estates")


def estate_new(request):
    form = EstateForm()

    return render(request, 'greenfield_form.html', {'form': form})


def estate_edit(request, uuid):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EstateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    else:
        estate = find_by_uuid(uuid)
        print(dir(estate))
        init_data = {
            "uuid": uuid,
            "property_name": estate.name,
            "donation": estate.donation,
            "location": estate.greenfieldlocation.geometry,
            "contact_firstname": estate.contact_person.first_name,
            "contact_lastname": estate.contact_person.last_name,
            "contact_role": estate.contact_person.role,
            "owner_type": estate.owner.type,
            "owner_name": estate.owner.name,
            "regional_plan": estate.spatial_plan,
            "parcel_numbers": estate.parcel_numbers,
            "total_area": estate.total_area,
            "build_area": estate.build_area,
            "free_area": estate.free_area,
            "can_devide": estate.can_divide,
            "smallest_devided_unit": estate.smallest_divide_size,
            "available_since": estate.available_since,
            "currency": estate.currency,
            "selling_price_minimal": estate.selling_price_minimal,
            "selling_price_maximal": estate.selling_price_maximal,
            "renting_price_minimal": estate.rental_price_minimal,
            "renting_price_maximal": estate.rental_price_maximal,
            "service_costs": estate.service_price,
            "price_note": estate.price_note,
            "agricultural_fund": estate.agricultural_fund,
            "af_removal_price": estate.af_removal_price,
            "previous_usage": estate.previous_usage,
            "hydrogeological_survey": estate.hydrogeological_survey,
            "ground_water_level": estate.water_level,
            "note": estate.note,
            "ecological_stress": estate.ecological_stress,
            "number_of_levels": estate.levels,
            "heigth": estate.height,
            "security": estate.security,
            "fire_protection": estate.fire_protection,
            "heating": estate.heating,
            "air_condition": estate.air_condition,
            "crane": estate.crane,
            "reception_desk": estate.reception_desk,
            "parking_place": estate.parking_place,
            "load_lift": estate.load_lift,
            "personal_lift": estate.personal_lift,
            "canteen": estate.canteen,
            "railway_siding": estate.railway_siding,
            "other_equipment": estate.other_equipment,
        }

        form = EstateForm(initial=init_data)
        return render(request, 'greenfield_form.html', {'form': form,
                                                        'estate': estate})


def estate_render(request, uuid):

    estate = find_by_uuid(uuid)

    return HttpResponse(estate)


def find_by_uuid(uuid):

    for obj_type in ALL_TYPES:
        try:
            return obj_type.objects.get(uuid=uuid)
        except ObjectDoesNotExist as e:
            continue
    raise ObjectDoesNotExist("{} uuid does not identify any object".format(uuid))

