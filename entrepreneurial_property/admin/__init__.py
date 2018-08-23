from django.contrib import admin

from ..models import ContactPerson
from ..models import Owner
from ..models import GreenField
from ..models import DevelopmentPark
from ..models import IndustrialAreal
from ..models import Office
from ..models import ScientificPark
from ..models import Brownfield

from .greenfield import GreenFieldAdmin
from .developmentpark import DevelopmentParkAdmin
from .industrialareal import IndustrialArealAdmin
from .office import OfficeAdmin
from .scientificpark import ScientificParkAdmin
from .brownfield import BrownfieldAdmin


admin.site.register(GreenField, GreenFieldAdmin)
admin.site.register(DevelopmentPark, DevelopmentParkAdmin)
admin.site.register(IndustrialAreal, IndustrialArealAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(ScientificPark, ScientificParkAdmin)
admin.site.register(Brownfield, BrownfieldAdmin)
admin.site.register(Owner)
admin.site.register(ContactPerson)
