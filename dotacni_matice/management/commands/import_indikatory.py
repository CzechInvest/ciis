from django.core.management.base import BaseCommand, CommandError
from dotacni_matice.models.indicators import *
from openpyxl import load_workbook
import datetime
import re

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def add_arguments(self, parser):
        parser.add_argument('data', type=str, help="data file")

    def handle(self, *args, **options):

        file_name = options["data"]
        wb = load_workbook(file_name)
        all_obj = self.indicators(wb, "Indikátory")
        #DotacniTitul.objects.bulk_create(all_obj)
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))

    def indicators(self, wb, tab):

        data = wb.get_sheet_by_name(tab)
        out_data = []

        counter = 0
        for row in data:
            counter += 1
            if counter <= 2:
                continue

            print(row[0])
            row = list(map(lambda x: self.clean(x), row))

            y = ("kod_nci_07_13", "npr_envi", "c_s", "fond", "kod_ek", "wf", "kod_nci_2014", "kod_sfc",
            "kod_sed", "op", "main_indicator", "sfc", "field_en", "field", "indicator_name_cs",
            "indicator_name_en", "unit", "type_", "definition", "frequency", "resource",
            "resource_comments", "data_source", "es_esf2014", "projects_number", "ec_comments")
                    

            x = (kod_nci_07_13, npr_envi, c_s, fond, kod_ek, wf, kod_nci_2014, kod_sfc,
            kod_sed, op, main_indicator, sfc, field_en, field, indicator_name_cs,
            indicator_name_en, unit, type_, definice, definition, frequency, resource,
            resource_comments, data_source, es_esf2014, projects_number, ec_comments) \
                    = row[0:27]

            #for i in range(len(x)):
            #    print(i, y[i], x[i])


            if npr_envi=="ENVI":
                npr_envi = True
            else:
                npr_envi = False

            if c_s:
                c_s = c_s.lower()


            if fond:
                fond = fond.replace(" ","")
                if fond == "EFRR/FS":
                    fond = "efrr_fs"
                elif fond == "ENRF":
                    fond = "enrf"
                elif fond == "ESF":
                    fond = "esf"
                elif fond == "ESF/YEI":
                    fond = "esf_yei"
                elif fond == "EUS":
                    fond = "eus"
                elif fond == "EZFRV":
                    fond = "ezfrv"
                else:
                    raise Exception(f"Fond |{fond}|")

            if not frequency:
                frequency = "průběžně"

            if wf:
                try:
                    wf = int(wf)
                except ValueError:
                    wf = None

            if kod_sed:
                kod_sed = self.get_objects(kod_sed, KodSed, "/", int, "kod")

            if op:
                op = self.get_objects(op, OP, ";", str, "op")

            if sfc:
                sfc = self.get_objects(sfc, OP, ";", str, "op")

            if main_indicator:
                main_indicator = self.get_objects(main_indicator, OP, ";", str,
                        "op")

            if field:
                field = self.get_objects(field, Field, "xxxx", str, "field")

            if data_source:
                data_source = self.get_objects(data_source, DataSource, "xxxx",
                        str, "source")[0]

            print("#######x", data_source)

            if not kod_nci_2014:
                continue

            if es_esf2014:
                es_esf2014 = True
            else:
                es_esf2014 = False

            if type_:
                if type_ == "kontext":
                    type_ = "context"
                elif type_ == "výstup":
                    type_ = "output"
                elif type_ == "výsledek":
                    type_ = "result"

            if kod_nci_2014 and int(kod_nci_2014) < 10:
                continue

            if not definice:
                if definition:
                    definice = definition
                else:
                    definice = ""

            fs = Indicator.objects.create(
                kod_nci_07_13=kod_nci_07_13,
                npr_envi=npr_envi,
                c_s=c_s,
                fond=fond,
                kod_ek=kod_ek,
                wf=wf,
                kod_nci_2014=kod_nci_2014,
                kod_sfc=kod_sfc,
                indicator_name_cs=indicator_name_cs,
                indicator_name_en=indicator_name_en,
                unit=unit,
                type=type_,
                definition=definice,
                frequency=frequency,
                resource=resource,
                resource_comments=resource_comments,
                data_source=data_source,
                es_esf2014=es_esf2014,
                projects_number=0,
                ec_comments=ec_comments
            )

            if kod_sed:
                for kod in kod_sed:
                    fs.kod_sed.add(kod)
            if op:
                for o in op:
                    fs.op.add(o)
            if sfc:
                for sf in sfc:
                    fs.sfc.add(sf)
            if main_indicator:
                for main in main_indicator:
                    fs.main_indicator.add(main)
            if field:
                for fiel in field:
                    fs.field.add(fiel)


    def get_objects(self, data, cls, sep, retype, attr):

            final_seds = []
            numbers = str(data).split(sep)
            for num in numbers:
                num = retype(num)
                args = {attr: num}
                seds = cls.objects.filter(**args)
                if len(seds) > 0:
                    final_seds.append(seds[0])
                else:
                    args = {attr: num}
                    final_seds.append(cls.objects.create(**args))

            return final_seds

    def clean(self, val):

        val = val.value

        if isinstance(val, str):
            val = val.strip()

        return val


    #kod_nci_07_13,
    #npr_envi,
    #c_s,
    #fond,
    #kod_ek,
    #wf,
    #kod_nci_2014,
    #kod_sfc,
    #kod_sed,
    #op,
    #main_indicator,
    #sfc,
    #field,
    #indicator_name_cs,
    #indicator_name_en,
    #unit,
    #type,
    #definition,
    #frequency,
    #resource,
    #resource_comments,
    #data_source,
    #es_esf2014,
    #projects_number,
    #ec_comments,
