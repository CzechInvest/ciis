from django.core.management.base import BaseCommand, CommandError
from socekon.models import Lau1Stats, Nuts3Stats
from cigeo.models import Lau1, Nuts3
from django.core.exceptions import ObjectDoesNotExist
from pathlib import Path
import json

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def handle(self, *args, **options):

        for cls, reg, files in ((Lau1Stats, Lau1, "okresy"), (Nuts3Stats, Nuts3, "kraje")):

            path = Path(Path(__file__).parent, "..",
                    "data", "soc_ekon-{}.json".format(files)).absolute()

            new_obj = []

            with open(path) as region:
                data = json.load(region)

            for f in data:
                kod = f["Kod"]
                rec = {}
                if kod > 0:

                    region = reg.objects.get(code=kod)
                    reg_name = None
                    if files == "okresy":
                        rec["lau1"] = region
                        reg_name = "lau1"
                        rec["population"] = f["Populace-okr"]
                        rec["work_power"] = f["Prac_síla-okr"]
                        rec["unemployment"] = f["Počet_nezam-okr"]
                        rec["unemployment_rate"] = f["Míra_nezam-okr"]
                        rec["unemployed_per_job"] = f["Počet_nezam_na_1_PM-okr"]
                    else:
                        rec["nuts3"] = region
                        reg_name = "nuts3"
                        rec["population"] = f["Populace"]
                        rec["work_power"] = f["Pracovní_síla"]
                        rec["unemployment"] = f["Počet_nezam"]
                        rec["unemployment_rate"] = f["Míra_nezam"]
                        rec["unemployed_per_job"] = f["Počet_nezam_na_prac_místo"]
                        rec["medium_salary"] = f["Mzdy"]

                    existing_objs = cls.objects.filter(**{reg_name: region})
                    if len(existing_objs) > 0:
                        print("updating")
                        existing_objs.update(**rec)
                    else:
                        print("newwww")
                        new_obj.append(cls(**rec))
            cls.objects.bulk_create(new_obj)
            self.stdout.write(self.style.SUCCESS('Successfully imported {} data'.format(files)))
