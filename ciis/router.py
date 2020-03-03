from rest_framework import routers
from socekon.api import viewsets as socekon_viewsets

router = routers.DefaultRouter()
router.register("socekon/nuts3", socekon_viewsets.Nuts3ViewSet)
router.register("socekon/lau1", socekon_viewsets.Lau1ViewSet)
