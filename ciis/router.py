from rest_framework import routers
from socekon.api import viewsets as socekon_viewsets
from cigeo.api import viewsets as cigeo_viewsets
from addresses.api import viewsets as addresses_viewsets
from rks.api import viewsets as rk_viewsets
from vtp.api import viewsets as vtp_viewsets
from django.conf.urls import url
from django.urls import include, path

router = routers.DefaultRouter()
router.register("socekon/nuts3", socekon_viewsets.Nuts3ViewSet, basename="api/socekon/nuts3")
router.register("socekon/lau1", socekon_viewsets.Lau1ViewSet, basename="api/socekon/lau1")
router.register("cigeo/nuts3", cigeo_viewsets.Nuts3ViewSet)
router.register("cigeo/lau1", cigeo_viewsets.Lau1ViewSet)
router.register("addresses", addresses_viewsets.AddressesViewSet)
router.register("vtp", vtp_viewsets.VtpViewSet)
router.register("rks", rk_viewsets.RKViewSet)

patterns = url(r'^api/', include(router.urls)),
