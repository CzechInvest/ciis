from django.core.management.base import BaseCommand, CommandError
from suppliers.models import Sector, Certificate

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def add_arguments(self, parser):
        parser.add_argument('address_archive', nargs='?', type=str)
        pass

    def handle(self, *args, **options):

        if options["address_archive"]:
            address_file = options["address_archive"]
        else:
            address_file = None

        self.import_certificates()
        self.import_sectors()

    def import_sectors(self):
        Sector.objects.bulk_create([
            Sector(name="Automobilový průmysl"),
            Sector(name="Letecký průmysl"),
            Sector(name="Elektronika a elektrotechnika"),
            Sector(name="Energetika"),
            Sector(name="ICT Informační a komunikační"),
            Sector(name="Zpracování kovů"),
            Sector(name="Výroba plastových výlisků a pryže"),
            Sector(name="Strojírenství"),
            Sector(name="Materiály a obaly"),
            Sector(name="Zdravotnická technika, biotechnologie a farmaceutický průmysl")
        ])
        self.stdout.write(self.style.SUCCESS('Successfully imported sectors data'))

    def import_certificates(self):
        Certificate.objects.bulk_create([
                Certificate(name="ISO 9001"),
                Certificate(name="ISO 9002"),
                Certificate(name="ISO 9001-2008"),
                Certificate(name="ISO 14 001"),
                Certificate(name="OHSAS 18 001"),
                Certificate(name="VDA"),
                Certificate(name="QS"),
                Certificate(name="ISO/TS 16949"),
                Certificate(name="EN 970 / ISO 17637"),
                Certificate(name="ISO 20807"),
                Certificate(name="NADCAP for NDT and AQS"),
                Certificate(name="SNECMA"),
                Certificate(name="ISO 5001:2011"),
                Certificate(name="DIN EN 14001:2005 "),
                Certificate(name="CQS 2040/2006"),
                Certificate(name="ČSN EN 729-2:1996"),
                Certificate(name="ČSN EN 124 "),
                Certificate(name="EN 13980"),
                Certificate(name="AS 9100"),
                Certificate(name="EN 9100")
        ])
        self.stdout.write(self.style.SUCCESS('Successfully imported certificate data'))
