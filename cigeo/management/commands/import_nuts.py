from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import GEOSGeometry
from cigeo.models import Lau1, Nuts3
import os
from django.contrib.gis.gdal import DataSource

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def handle(self, *args, **options):

        for cls, files in ((Lau1,"okresy"), (Nuts3, "kraje")):
            cls.objects.

            path = os.path.abspath(os.path.join(
                    os.path.dirname(__file__), "..",
                    "data", "{}.geojson".format(files)))

            ds = DataSource(path)

            layer = ds[0]
            all_obj = []

            for f in layer:
                geom = GEOSGeometry(f.geom.wkt)
                all_obj.append(
                        cls(
                            code=f.get("Kod"),
                            name=f.get("nazev"),
                            geometry=geom
                        )
                    )
            cls.objects.bulk_create(all_obj)
            self.stdout.write(self.style.SUCCESS('Successfully imported {} data'.format(files)))
