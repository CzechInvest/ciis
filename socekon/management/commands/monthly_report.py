"""
Materiál HR Přehled
* Podle kalendáře na MPSV se vždy stáhnou měsíční statistiky
    nezaměstnanosti z (https://www.mpsv.cz/web/cz/mesicni). V rámci zazipovaných
    dat daného měsíce se pro potřeby HR přehledu bere vždy tabulka č. 4. Zajímá nás
    uchazeči o zaměstnání celkem (bacha nebrat ze sloupce ženy), volná pracovní
    místa celkem a vždy ke konci sled. měsíce a podíl nezaměstnaných osob celkem.
* Uchazeči na 1 VPM se vypočítají vzorcem „uchazeči o zaměstnání děleno volná
    pracovní místa celkem“ (pokud nedojde ke změně zdrojové tabulky, tak stačí do
    té excelové tabulky překopírovat vzorec =J11/X11).
* Obyvatelstvo 15-64 let se bere z MPSV z oddílu
    https://www.mpsv.cz/web/cz/nezamestnanost-v-obcich podle okresů. Stačí vybrat
    nejnovější měsíc, kraj a konkrétní okres a dole opsat hodnotu z řádku celkem.
    Exporty jdou, ale není to s nima úplně jednoduchý. Spíš bych pracoval s těmi
    stránkami (platí obecně, nejen pro tato konkrétní čísla).
* Mzdy se berou z Českého statistického úřadu.
* Rozesílá se mailem na DIZA; STR; DSI; DPP; ZAK
* Aktualizuje se jen na disku K:


"""
from django.core.management.base import BaseCommand, CommandError
from socekon.models import HumanResourcesNuts3, HumanResourcesLau1, Date
from cigeo.models import Lau1, Nuts3
from django.core.exceptions import ObjectDoesNotExist
from pathlib import Path
import json
from openpyxl import load_workbook
import os
from collections import OrderedDict
import copy

from html.parser import HTMLParser
import requests
import tempfile
import atexit
import shutil
import zipfile
import sparql
import ssl
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

__FILES__ = []

def __remove_files__():

    global __FILES__
    return
    for f in __FILES__:
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)

atexit.register(__remove_files__)

class StatakHTMLParser(HTMLParser):

    def __init__(self, *args, **kwargs):
        self.tab3_link = None
        super(StatakHTMLParser, self).__init__(*args, **kwargs)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    if attr[1].find("_3.xlsx") > 0:
                        self.tab3_link = attr[1]

class Command(BaseCommand):
    help = 'Import HR data to Django from web services'

    def add_arguments(self, parser):
        parser.add_argument('date', type=str)

    def handle(self, *args, **options):

        nr_nuts3 = 0
        nr_lau1 = 0

        thedate = options["date"]
        (year, month, day) = thedate.split("-")
        #month, year = (int(month), int(year))

        unemployment_data = self._get_unemployment(year, month)
        resources_data = self._get_jobs(unemployment_data["kraje"], year, month)
        data = self.merge(unemployment_data, resources_data)
        wages_nuts3 = self._get_stats_link(year, month)

        self.import_data(data, wages_nuts3, year, month)

    @staticmethod
    def import_lau1(data, year, month):
        for lau1 in data:
            print("""
            lau1={lau1},
            date={date{,
            inhabitans={inhabitans},
            productive_inhabitans={productive_inhabitans},
            unemployment={unemployment},
            vacanies={vacancies},
            unemployment={unemployment},
            applications_per_vacancy={applications_per_vacancy},
            """)
        print(data[lau1])


    @staticmethod
    def import_data(data, wages_nuts3, year, month):

        self.import_lau1(data["okresy"], year, month)


    @staticmethod
    def _get_stats_link(year, month):
        global __FILES__
        print(year, month)
        month = int(month)

        q = 1
        if month <= 3:
            q = 1
        elif month <= 6:
            q = 2
        elif month <= 9:
            q = 3
        elif month <= 12:
            q = 4

        parser = StatakHTMLParser()

        while not parser.tab3_link:
            link = "https://statistika.info/csu/czso/cri/prumerne-mzdy-{}-ctvrtleti-{}".format(q, year)
            response = requests.get(link, verify=False)
            parser.feed(response.content.decode("utf-8"))

            if not parser.tab3_link:
                q = q - 1
                if q < 1:
                    q = 4
                    year  = int(year) - 1

        assert parser.tab3_link

        (fd, wages_quartal_filename) = tempfile.mkstemp(prefix="wages-", suffix=".xlsx")
        __FILES__.append(wages_quartal_filename)

        response = requests.get(parser.tab3_link)
        with open(wages_quartal_filename, "wb") as out:
            out.write(response.content)

        wb = load_workbook(wages_quartal_filename)
        data_sheet = wb.get_sheet_by_name("List1")
        all_data = list(data_sheet.values)[9:31]
        data = {}

        for row in all_data:
            data[row[0]] = row[4]
        return data

    def _merge_type(self, unempl, resource, mytype):

        data = {}
        for name in unempl[mytype]:
            if name == "Praha" and mytype == "okresy":
                continue
            if name in resource[mytype]:
                print(name)
                data[name] = OrderedDict(
                    #inhabitans=
                    name=name,
                    productive_inhabitans=resource[mytype][name]["obyvatelstvo15_64"],
                    unemployed=unempl[mytype][name]["unemployed"],
                    vacancies=unempl[mytype][name]["vacancies"],
                    unemployment=unempl[mytype][name]["unemployment"],
                    applications_per_vacancy=unempl[mytype][name]["applications_per_vacancy"]
                )
        return data

    def merge(self, unempl, resource):
        okresy = self._merge_type(unempl, resource, "okresy")
        kraje = self._merge_type(unempl, resource, "kraje")
        print(kraje)
        return {"kraje": kraje, "okresy": okresy}


    def _get_unemployment(self,year, month):
        global __FILES__
        response = requests.get("https://www.mpsv.cz/o/rest/statistiky/nezamestnanost/{}/{}".format(year,
            month))

        thedir = tempfile.mkdtemp(prefix="unemployment-")
        __FILES__.append(thedir)

        unemployment_zip = os.path.join(thedir, "{}-{}.zip".format(year, month))
        unemployment_excel =  os.path.join(thedir, "4. NEZ{}{}h.xlsx".format(month, int(year)-2000))

        with open(unemployment_zip, "bw") as out_zip:
            out_zip.write(response.content)

        zipfile_class = zipfile.ZipFile(unemployment_zip)
        zipfile_class.extract(os.path.basename(unemployment_excel), path=thedir)

        assert os.path.isfile(unemployment_excel)

        wb = load_workbook(unemployment_excel)
        data_sheet = wb.get_sheet_by_name("nuts3")
        all_data = list(data_sheet.values)[10:100]
        data = {"okresy":{}, "kraje":{}}

        okresy_in_kraj = []
        for row in all_data:
            name = row[1]
            unemployed = row[9]
            vacancies = row[23]
            unemployment = row[29]
            applications_per_vacancy = unemployed / vacancies

            record = {
                'name': name,
                'unemployed': unemployed,
                'vacancies': vacancies,
                'unemployment': unemployment,
                'applications_per_vacancy': applications_per_vacancy
            }

            if name.lower().find("kraj") > -1:
                data["kraje"][name] = record
                data["kraje"][name]["okresy"] = copy.copy(okresy_in_kraj)
                okresy_in_kraj = []
            else:
                okresy_in_kraj.append(name)
                data["okresy"][name] = record
        return data



    def _get_jobs(self, kraje, year, month):

        data = (
            "PREFIX zdroj: <https://data.mpsv.cz/zdroj/>\n"
            "PREFIX pojem: <https://data.mpsv.cz/pojem/>\n"
            "PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n"
            "SELECT \n"
            "SUM(?uchazeciOZamestnani) AS ?uchazeciOZamestnani\n"
            "SUM(?dosazitelniUchazeci) AS ?dosazitelniUchazeci\n"
            "SUM(?podilNezamestnanychOsob) AS ?podilNezamestnanychOsob\n"
            "SUM(?volnaPracovnaMista) AS ?volnaPracovnaMista\n"
            "SUM(?obyvatelstvo15_64) AS ?obyvatelstvo15_64\n"
            "?nazevObce\n"
            "?nazevOkresu\n"
            "?rok\n"
            "?mesic\n"
            "FROM zdroj:NezamestnanostVObcich\n"
            "FROM NAMED zdroj:Okresy\n"
            "FROM NAMED zdroj:Kraje\n"
            "FROM NAMED zdroj:Obce\n"
            "WHERE \n"
            "{{\n"
            "?polozka pojem:mesic ?mesic .\n"
            "FILTER (MONTH(?mesic) = {month})\n"
            "?polozka pojem:rok ?rok .\n"
            "FILTER (YEAR(?rok) = {year})\n"
            "?polozka pojem:okres ?idOkresu .\n"
            "?polozka pojem:obec ?idObce .\n"
            "?polozka pojem:dosazitelniUchazeci ?dosazitelniUchazeci .\n"
            "?polozka pojem:podilNezamestnanychOsob ?podilNezamestnanychOsob .\n"
            "?polozka pojem:uchazeciOZamestnani ?uchazeciOZamestnani .\n"
            "?polozka pojem:volnaPracovnaMista ?volnaPracovnaMista .\n"
            "?polozka pojem:obyvatelstvo15_64 ?obyvatelstvo15_64\n"
            "GRAPH zdroj:Okresy\n"
            "{{\n"
            "?idOkresu skos:prefLabel ?nazevOkresu .\n"
            "?idOkresu pojem:kraj ?idKraje\n"
            "}}\n"
            "GRAPH zdroj:Kraje\n"
            "{{\n"
            "?idKraje skos:prefLabel ?nazevKraje\n"
            "}}\n"
            "GRAPH zdroj:Obce\n"
            "{{\n"
            "?idObce skos:prefLabel ?nazevObce\n"
            "}}\n"
            "}}\n"
            "GROUP BY ?rok ?mesic ?nazevObce ?nazevOkresu\n"
            "ORDER BY DESC(?rok), DESC(?mesic), ASC(?nazevObce), ASC(?nazevOkresu)"
            ).format(month=month, year=year)
        s = sparql.Service("https://www.mpsv.cz/sparql/", "utf-8", "POST",
                           accept='application/json')
        result = s.query(data, raw=True)
        #response = requests.post("https://www.mpsv.cz/sparql/", data=data,
        #        headers={"Accept": "application/json"})
        data = json.load(result)
        head = data["head"]
        data = data["results"]

        okresy = {}
        newkraje = {}
        for obec in data["bindings"]:

            nazevOkresu = obec["nazevOkresu"]["value"]
            if nazevOkresu == "Plzeň":
                nazevOkresu = "Plzeň-město"
            if nazevOkresu == "Ostrava":
                nazevOkresu = "Ostrava-město"
            if nazevOkresu == "Hlavní město Praha":
                nazevOkresu = "Praha"
            kraj = self._get_kraj_name(nazevOkresu, kraje)
            assert kraj

            if not nazevOkresu in okresy:
                okresy[nazevOkresu] = {}
                okresy[nazevOkresu]["uchazeciOZamestnani"] = 0
                okresy[nazevOkresu]["dosazitelniUchazeci"] = 0
                okresy[nazevOkresu]["volnaPracovnaMista"] = 0
                okresy[nazevOkresu]["obyvatelstvo15_64"] = 0

            if not kraj in newkraje:
                newkraje[kraj] = {}
                newkraje[kraj]["uchazeciOZamestnani"] = 0
                newkraje[kraj]["dosazitelniUchazeci"] = 0
                newkraje[kraj]["volnaPracovnaMista"] = 0
                newkraje[kraj]["obyvatelstvo15_64"] = 0

            okresy[nazevOkresu]["uchazeciOZamestnani"] += int(obec["uchazeciOZamestnani"]["value"])
            okresy[nazevOkresu]["dosazitelniUchazeci"] += int(obec["dosazitelniUchazeci"]["value"])
            okresy[nazevOkresu]["volnaPracovnaMista"] += int(obec["volnaPracovnaMista"]["value"])
            okresy[nazevOkresu]["obyvatelstvo15_64"] += int(obec["obyvatelstvo15_64"]["value"])

            newkraje[kraj]["uchazeciOZamestnani"] += int(obec["uchazeciOZamestnani"]["value"])
            newkraje[kraj]["dosazitelniUchazeci"] += int(obec["dosazitelniUchazeci"]["value"])
            newkraje[kraj]["volnaPracovnaMista"] += int(obec["volnaPracovnaMista"]["value"])
            newkraje[kraj]["obyvatelstvo15_64"] += int(obec["obyvatelstvo15_64"]["value"])


        return {"okresy": okresy, "kraje": newkraje}

    def _get_kraj_name(self, okres, kraje):

        for kraj in kraje:
            if okres in kraje[kraj]["okresy"]:
                return kraj
