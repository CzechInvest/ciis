from django.core.management.base import BaseCommand, CommandError
from socekon.models import HumanResourcesNuts3, HumanResourcesLau1, Date
from cigeo.models import Lau1, Nuts3
from django.core.exceptions import ObjectDoesNotExist
from pathlib import Path
import json
from openpyxl import load_workbook

class Command(BaseCommand):
    help = 'Import HR data to Django from Excel shiit '

    def add_arguments(self, parser):
        parser.add_argument('input_file', type=str)
        parser.add_argument('date', type=str)

    def handle(self, *args, **options):

        input_file = options["input_file"]
        file_date = options["date"]
        
        wb = load_workbook(input_file)
        data_sheet = wb.get_sheet_by_name("Lidské zdroje")
        all_data = list(data_sheet.values)[7:97]
        dates = Date.objects.filter(date=file_date)

        laus_recs = []
        nuts_recs = []

        if dates:
            new_date = dates[0]
        else:
            new_date = Date.objects.create(date=file_date)
        for row in all_data:
            (name, inhabitans, prod_inhabitans, unemployed, free, unemployment,
                    applicants, reward) = row[1:9]

            if name == "Praha":
                name = "Hlavní město Praha"
            laus1 = Lau1.objects.filter(name = name)
            nuts3 = Nuts3.objects.filter(name = name)

            if laus1:
                lau1 = laus1[0]
                laus_recs.append(
                    HumanResourcesLau1(
                        lau1=lau1,
                        date=new_date,
                        inhabitans=int(inhabitans),
                        productive_inhabitans=int(prod_inhabitans),
                        unemployed=int(unemployed),
                        vacancies=int(free),
                        unemployment=float(unemployment),
                        applications_per_vacancy=int(applicants)
                    )
                )
            elif nuts3:
                nut3 = nuts3[0]
                nuts_recs.append(
                    HumanResourcesNuts3(
                        nuts3=nut3,
                        date=new_date,
                        inhabitans=int(inhabitans),
                        productive_inhabitans=int(prod_inhabitans),
                        unemployed=int(unemployed),
                        vacancies=int(free),
                        unemployment=float(unemployment),
                        applications_per_vacancy=int(applicants),
                        wages=int(reward)
                    )
                )
            
            else:
                print(name)

        HumanResourcesNuts3.objects.bulk_create(nuts_recs)
        HumanResourcesLau1.objects.bulk_create(laus_recs)
        self.stdout.write(self.style.SUCCESS('Successfully imported {} data'.format(input_file)))
