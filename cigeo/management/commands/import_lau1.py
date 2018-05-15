from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import GEOSGeometry
from cigeo.models import Lau1
import os
from django.contrib.gis.gdal import DataSource

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def handle(self, *args, **options):

        path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..",
                "data", "okresy.geojson"))

        ds = DataSource(path)

        layer = ds[0]
        all_lau1 = []

        for f in layer:
            geom = GEOSGeometry(f.geom.wkt)
            all_lau1.append(
                    Lau1(
                        code=f.get("Kod"),
                        name=f.get("nazev"),
                        geometry=geom
                    )
                )

        Lau1.objects.bulk_create(all_lau1)
        self.stdout.write(self.style.SUCCESS('Successfully imported LAU-1 data'))
