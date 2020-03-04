from rest_framework import routers
from socekon.api import viewsets as socekon_viewsets
from cigeo.api import viewsets as cigeo_viewsets
from addresses.api import viewsets as addresses_viewsets

router = routers.DefaultRouter()
router.register("socekon/nuts3", socekon_viewsets.Nuts3ViewSet)
router.register("socekon/lau1", socekon_viewsets.Lau1ViewSet)
router.register("cigeo/nuts3", cigeo_viewsets.Nuts3ViewSet)
router.register("cigeo/lau1", cigeo_viewsets.Lau1ViewSet)
router.register("addresses", addresses_viewsets.AddressesViewSet)
