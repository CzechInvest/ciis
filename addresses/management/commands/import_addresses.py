from django.core.management.base import BaseCommand, CommandError
from addresses.models import Address, City
import tempfile
import requests
import zipfile

import csv
import os
from pyproj import Proj, transform
import fiona
from fiona.crs import from_epsg
from django.contrib.gis.geos import GEOSGeometry
import shutil

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def add_arguments(self, parser):
        parser.add_argument('address_archive', nargs='?', type=str)
        pass

    def handle(self, *args, **options):

        if options["address_archive"]:
            address_file = options["address_archive"]
        else:
            address_file = None

        self.import_addresses(address_file)

    def import_addresses(self, address_file):

            tempdir = tempfile.mkdtemp(prefix="tmp-ciis-")

            if not address_file:
                self.stdout.write("Downloading data from CUZK")
                response = requests.get('http://vdp.cuzk.cz/vymenny_format/csv/20171031_OB_ADR_csv.zip', stream=True)

                # Throw an error for bad status codes
                response.raise_for_status()

                output_zip = os.path.join(tempdir, 'adress_points.zip')

                with open(output_zip, 'wb') as handle:
                    for block in response.iter_content(1024):
                        handle.write(block)
            else:
                self.stdout.write("Using existing archive {}".format(address_file))
                output_zip = address_file

            with zipfile.ZipFile(output_zip) as zf:
                zf.extractall(path=tempdir)

            original = Proj("""+proj=krovak +lat_0=49.5 +lon_0=24.83333333333333
                               +alpha=30.28813972222222 +k=0.9999 +x_0=0 +y_0=0
                               +ellps=bessel
                               +towgs84=507.8,85.7,462.8,4.998,1.587,5.261,3.56
                               +units=m +no_defs""")
            dest = Proj("+proj=longlat +datum=WGS84 +no_defs")

            path = os.path.join(tempdir, "CSV")

            self.stdout.write("Importing data to database")

            for f in os.listdir(path):
                all_addresses = []
                f = os.path.join(path, f)
                obec_obj = None
                with open(f, encoding="windows-1250") as csv_f:
                    reader = csv.reader(csv_f, delimiter=";")
                    first = True
                    second = True
                    for row in reader:
                        if first:
                            first = False
                            continue

                        (kod_adm, kod_obec, obec,
                         momc, mop, cast_obce_kod, cast_obce,
                         ulice, so, cislo_domovni, cislo_orientacni,
                         znak_c_orientacniho,
                         psc, y, x, od) = row

                        if second:
                            second = False
                            obec_obj = City.objects.create(code=int(kod_obec), name=obec)

                        if x and y:
                            lon, lat = transform(original, dest,-1*float(y),-1*float(x))
                            coords = GEOSGeometry('POINT({} {})'.format(lon, lat), srid=4326) #
                        else:
                            coords = None

                        all_addresses.append(
                        Address(
                               adm=int(kod_adm),
                               street=ulice,
                               house_number=cislo_domovni,
                               orientation_number=cislo_orientacni,
                               city=obec_obj,
                               zipcode=psc,
                               coordinates=coords)
                        )

                Address.objects.bulk_create(all_addresses)
                self.stdout.write('Successfully imported address data {}'.format(f))


            shutil.rmtree(tempdir)
            self.stdout.write(self.style.SUCCESS('Successfully imported address data'))
