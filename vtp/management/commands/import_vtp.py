from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import GEOSGeometry
from vtp.models import VtpType, Service, Vtp
from django.contrib.gis.gdal import DataSource
from addresses.tools import geocode
from addresses.models import Address
import json

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def add_arguments(self, parser):
        parser.add_argument('input', type=str, help="GeoJson file")

    def handle(self, *args, **options):

        Vtp.objects.all().delete()
        with open(options["input"]) as inpt:
            data = json.load(inpt)

            features = data["features"]

            for f in features:

                addressid = geocode(f["properties"]["address"])
                address = Address.objects.get(adm=addressid)

                vtp = Vtp.objects.create(name=f["properties"]["name"],
                         url=f["properties"]["url"],
                         address=address)

                for s in f["properties"]["services"]:
                    services = Service.objects.filter(service=s)
                    if len(services):
                        vtp.services.add(services[0])
                        pass
                    else:
                        service = Service.objects.create(service=s)
                        vtp.services.add(service)
                        pass
                for t in f["properties"]["type"]:
                    types = VtpType.objects.filter(type=t)
                    if len(types):
                        vtp.type.add(types[0])
                        pass
                    else:
                        typ = VtpType.objects.create(type=t)
                        vtp.type.add(typ)
                        pass
