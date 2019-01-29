from django.core.management.base import BaseCommand, CommandError
from openpyxl import load_workbook
from whoiswho.models import Institution
from whoiswho.models import WhoIsWho
from whoiswho.models import ContactPerson
from whoiswho.models import Keyword
from whoiswho.models import Sector
from addresses.models import Address
from django.utils import timezone


class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def add_arguments(self, parser):
        parser.add_argument('whoiswho_export',  type=str)
        pass

    def handle(self, *args, **options):

        whoiswho_file = options["whoiswho_export"]

        self.import_whoiswho(whoiswho_file)

    def import_whoiswho(self, exportfile):

        wb = load_workbook(exportfile)
        sheet = wb.get_sheet_by_name("WiW")
        data = list(sheet.values)

        institutions = []
        contact_persons = []
        keyword_list = []
        sectors = []

        for row in data[1:]:
            (institution1, institution2, legal_form, web, adresni_body, address_1,
            city, zipcode, region, ICO, last_name, first_name, position, phone,
            mail, specialization, profile, keywords, sector, sector_code, notes) =  row[:21]

            if not adresni_body:
                continue
            ICO = str(ICO).split("_")[0]

            if not web:
                web=""

            if web.find("http") != 0:
                web = "http://"+web

            institutions = Institution.objects.filter(ico=ICO)
            if not institutions:
                legal_form_id, text = legal_form.split(" - ")

                institution = Institution(
                    name=institution1,
                    name_en = institution2,
                    legal_form = legal_form_id,
                    ico=ICO,
                    url=web,
                    address=Address.objects.get(adm=int(str(adresni_body).replace("AD.", "")))
                )

                institution.save()
            else:
                institution = institutions[0]

            if not position:
                position = ""
            if not first_name:
                first_name = ""
            if not last_name:
                last_name = ""
            if not mail:
                print(institution, first_name, last_name)

            contact_persons = ContactPerson.objects.filter(email=mail)
            if not contact_persons:
                person = ContactPerson(
                    first_name=first_name,
                    last_name=last_name,
                    email=mail,
                    phone=phone,
                    role=position,
                    crm="")
                person.save()
            else:
                person = contact_persons[0]

            use_keywords = []
            if keywords:
                my_keywords = keywords.split(",")
                for kw in my_keywords:
                    if not kw:
                        continue
                    kw = kw.lower().strip()
                    found_keywords = Keyword.objects.filter(kw=kw)
                    if not found_keywords:
                        mykw = Keyword(kw=kw)
                        mykw.save()
                        use_keywords.append(mykw)
                    else:
                        use_keywords.append(found_keywords[0])

            use_sectors = []
            if sector_code:
                my_sectors = sector_code.split()
                my_sectors_long = sector.split(", ")
                for sec in my_sectors:
                    if not sec:
                        continue
                    found_sectors = Sector.objects.filter(code=sec)
                    if not found_sectors:
                        idx = my_sectors.index(sec)
                        mysec = Sector(code=sec, name=my_sectors_long[idx].strip())
                        mysec.save()
                        use_sectors.append(mysec)
                    else:
                        use_sectors.append(found_sectors[0])

            if not profile:
                profile = ""
            if not notes:
                notes = ""
            if not specialization:
                specialization = ""

            whoiswho = WhoIsWho(
                institution=institution,
                contact_person=person,
                profile=profile,
                specialization=specialization,
                modified=timezone.now(),
                notes=notes
            )
            whoiswho.save()
            whoiswho.keywords.set(use_keywords)
            whoiswho.sectors.set(use_sectors)
        self.stdout.write('Successfully imported whoiswho data')
