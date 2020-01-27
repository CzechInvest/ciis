from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import GEOSGeometry
from vtp.models import VtpType, Service, Vtp
from django.contrib.gis.gdal import DataSource
from addresses.tools import geocode
import json

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def add_arguments(self, parser):
        parser.add_argument('input', type=str, help="GeoJson file")

    def handle(self, *args, **options):

        with open(options["input"]) as inpt:
            data = json.load(inpt)

            features = data["features"]

            for f in features:
                #vtp = Vtp(name=f["properties"]["name"],
                #          url=f["properties"]["url"])
                address = geocode(f["properties"]["address"])
                #for s in f["properties"]["service"]:
                #    services = Service.objects.filter(service=s)
                #    if len(services):
                #        vtp.services.append(services[0])
                #    else:
                #        service = Service(service=s)
                #        vtp.services.append(service)
                #for t in f["properties"]["type"]:
                #    types = VtpType.objects.filter(type=t)
                #    if len(types):
                #        vtp.services.append(types[0])
                #    else:
                #        typ = VtpType(type=t)
                #        vtp.type.append(typ)


                #print(f["properties"]["name"])
                print(address)
