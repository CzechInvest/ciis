from django.contrib import admin
from cigeo.models import Location
from .models import RealEstate
from .models import RealEstateType
from .models import Attachment
from .models import Photo
from .models import Keyword
from .models import Electricity
from .models import DrinkingWater
from .models import NonPotableWater
from .models import Gas
from .models import WasteWater
from .models import Telecommunications
from .models import Area
from .models import Ownership
from .models import Purpose
from .models import AreaArea
from .models import AreaPrice
from .models import Building
from .models import BuildingArea
from .models import BuildingDisposal
from .models import BuildingPrice
from .models import Floor


class RealEstateAdmin(admin.ModelAdmin):
    #raw_id_fields = ("location",)
    search_fields = ("title",)

# Register your models here.
admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Photo)
admin.site.register(Attachment)
admin.site.register(Keyword)
admin.site.register(RealEstateType)
admin.site.register(Electricity)
admin.site.register(DrinkingWater)
admin.site.register(NonPotableWater)
admin.site.register(Gas)
admin.site.register(WasteWater)
admin.site.register(Telecommunications)
admin.site.register(Area)
admin.site.register(Ownership)
admin.site.register(Purpose)
admin.site.register(AreaArea)
admin.site.register(AreaPrice)
admin.site.register(Building)
admin.site.register(BuildingArea)
admin.site.register(BuildingPrice)
admin.site.register(BuildingDisposal)
admin.site.register(Floor)
