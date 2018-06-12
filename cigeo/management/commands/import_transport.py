from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import GEOSGeometry
from cigeo.models import Road
import os
import fiona
from shapely.geometry import shape

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def handle(self, *args, **options):


        path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "..",
                "data", "gis_osm_roads_free.gpkg"))

        with fiona.open(path) as roads:

            all_obj = []
            count = 0
            max_count = 100000

            for f in roads:
                count += 1

                shapely_geom = shape(f["geometry"])
                geom = GEOSGeometry(shapely_geom.wkt)

                if f["properties"]["oneway"] == "yes":
                    oneway = True
                else:
                    oneway = False

                all_obj.append(
                        Road(
                            geometry=geom,
                            osm_id = f["properties"]["osm_id"],
                            code = f["properties"]["code"],
                            fclass = f["properties"]["fclass"],
                            name = f["properties"]["name"],
                            ref = f["properties"]["ref"],
                            oneway = oneway,
                            maxspeed = f["properties"]["maxspeed"],
                        )
                    )
                if count%max_count == 0 or count == len(roads):
                    Road.objects.bulk_create(all_obj)
                    all_obj = []
                    self.stdout.write(self.style.SUCCESS('Successfully imported {}/{}'.format(count, len(roads))))


        self.stdout.write(self.style.SUCCESS('Successfully imported all data'))
