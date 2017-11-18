from django.core.management.base import BaseCommand, CommandError
from infrastructure.models import Industry, Service, InfType

class Command(BaseCommand):
    help = 'Import initial data sets to database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        self.import_infrastructure_type()
        self.import_services()
        self.import_industries()


    def import_industries(self):
        Industry.objects.bulk_create([
                Industry(name="Technology"),
                Industry(name="ICT"),
                Industry(name="Innovation"),
                Industry(name="Social media"),
                Industry(name="Automotive"),
                Industry(name="Materiálové inženýrství"),
                Industry(name="ICT Life Sciences"),
                Industry(name="Elektronika a elektrotechnika"),
                Industry(name="Strojírenství")
        ])
        self.stdout.write(self.style.SUCCESS('Successfully imported industry data'))

    def import_infrastructure_type(self):
        InfType.objects.bulk_create([
                InfType(name="Incubator"),
                InfType(name="Accelerator"),
                InfType(name="VTP"),
                InfType(name="Co-working"),
        ])
        self.stdout.write(self.style.SUCCESS('Successfully imported infrastruture type data'))

    def import_services(self):
        Service.objects.bulk_create([
                Service(name="co-working"),
                Service(name="mentoring"),
                Service(name="equipment"),
                Service(name="networking"),
                Service(name="advisory"),
                Service(name="cooperation with industry/university"),
        ])
        self.stdout.write(self.style.SUCCESS('Successfully imported service data'))
