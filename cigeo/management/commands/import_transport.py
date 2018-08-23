from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import GEOSGeometry
from cigeo.models import Road
from cigeo.models import Airport
from cigeo.models import PublicTransportStop
from cigeo.models import RailwayStation
import os
import fiona
from shapely.geometry import shape
import requests
import atexit
import tempfile
import shutil
import zipfile
import json

TEMPDIR=tempfile.mkdtemp()

def clear():
    shutil.rmtree(TEMPDIR)

atexit.register(clear)

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def handle(self, *args, **options):

        self.stdout.write("Downloading data from OSM")
        resp = requests.get("http://download.geofabrik.de/europe/czech-republic-latest-free.shp.zip",
                            stream=True)
        zip_file = os.path.join(TEMPDIR, "czechrep.zip")
        with open(zip_file, 'wb') as fd:
            for chunk in resp.iter_content(chunk_size=1024):
                fd.write(chunk)
        #zip_file = "/home/jachym/Stažené/czech-republic-latest-free.shp.zip"

        self._import_roads(zip_file)
        self._import_airports()
        self._import_transport(zip_file)
        self.stdout.write(self.style.SUCCESS('Successfully imported all data'))

    def _import_airports(self):
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
        data_file = os.path.join(data_dir, 'airports.geojson')

        airports = []
        with open(data_file) as data_file:
            data = json.load(data_file)
            for feature in data['features']:

                shapely_geom = shape(feature["geometry"])
                geom = GEOSGeometry(shapely_geom.wkt)

                airport = Airport(
                    geometry=geom,
                    name=feature["properties"]["name"],
                    iata=feature["properties"]["iata"]
                )

                airports.append(airport)
        Airport.objects.bulk_create(airports)
        self.stdout.write(self.style.SUCCESS('Successfully imported airports'))

    def _import_transport(self, zip_file):

        data_file = zipfile.ZipFile(zip_file)
        for f in ("gis_osm_transport_free_1.cpg", "gis_osm_transport_free_1.dbf",
                  "gis_osm_transport_free_1.prj", "gis_osm_transport_free_1.shp",
                  "gis_osm_transport_free_1.shx"):
            data_file.extract(f, path=TEMPDIR)

        path = os.path.abspath(os.path.join(TEMPDIR, "gis_osm_transport_free_1.shp"))

        with fiona.open(path) as transport:
            all_obj = []
            count = 0
            max_count = 100000

            for f in transport:
                count += 1

                shapely_geom = shape(f["geometry"])
                geom = GEOSGeometry(shapely_geom.wkt)

                if f["properties"]["fclass"].endswith('_stop'):

                    all_obj.append(
                            PublicTransportStop(
                                geometry=geom,
                                name=f["properties"]["name"],
                                fclass=f["properties"]["fclass"],
                            )
                        )

                if count%max_count == 0 or count == len(transport):
                    PublicTransportStop.objects.bulk_create(all_obj)
                    all_obj = []
                    self.stdout.write(self.style.SUCCESS('Successfully imported {}/{}'.format(count, len(transport))))

        with fiona.open(path) as transport:
            railway_stations = []

            for f in transport:

                shapely_geom = shape(f["geometry"])
                geom = GEOSGeometry(shapely_geom.wkt)

                if f["properties"]["fclass"] == 'railway_station':

                    railway_stations.append(
                            RailwayStation(
                                geometry=geom,
                                name=f["properties"]["name"],
                                fclass=f["properties"]["fclass"],
                            )
                        )

            RailwayStation.objects.bulk_create(railway_stations)

    def _import_roads(self, zip_file):

        data_file = zipfile.ZipFile(zip_file)
        for f in ("gis_osm_roads_free_1.cpg", "gis_osm_roads_free_1.dbf",
                  "gis_osm_roads_free_1.prj", "gis_osm_roads_free_1.shp",
                  "gis_osm_roads_free_1.shx"):
            data_file.extract(f, path=TEMPDIR)

        path = os.path.abspath(os.path.join(TEMPDIR, "gis_osm_roads_free_1.shp"))

        with fiona.open(path) as roads:

            all_obj = []
            count = 0
            max_count = 100000

            for f in roads:
                count += 1

                shapely_geom = shape(f["geometry"])
                geom = GEOSGeometry(shapely_geom.wkt)

                if "oneway" in f["properties"] and f["properties"]["oneway"] == "yes":
                    oneway = True
                else:
                    oneway = False

                all_obj.append(
                        Road(
                            geometry=geom,
                            osm_id=f["properties"]["osm_id"],
                            code=f["properties"]["code"],
                            fclass=f["properties"]["fclass"],
                            name=f["properties"]["name"],
                            ref=f["properties"]["ref"],
                            oneway=oneway,
                            maxspeed=f["properties"]["maxspeed"],
                        )
                    )
                if count%max_count == 0 or count == len(roads):
                    Road.objects.bulk_create(all_obj)
                    all_obj = []
                    self.stdout.write(self.style.SUCCESS('Successfully imported {}/{}'.format(count, len(roads))))


