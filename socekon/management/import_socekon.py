from django.core.management.base import BaseCommand, CommandError
from socekon.models import Nuts3Stats, Lau1Stats
import os

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def handle(self, *args, **options):

        for cls, files in ((Lau1,"okresy"), (Nuts3Stats, "kraje")):

            path = os.path.abspath(os.path.join(
                    os.path.dirname(__file__), "..",
                    "data", "soc_ekon-{}.json".format(files)))

            with open(path) as regions:
                data = json.load(regions)

            nuts_data = []
            for record in data:

                all_obj.append(
                        cls(
                            code=f.get("Kod"),
                            name=f.get("nazev"),
                            geometry=geom
                        )
                    )
            cls.objects.bulk_create(all_obj)
            self.stdout.write(self.style.SUCCESS('Successfully imported {} data'.format(files)))
