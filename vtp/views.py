from .models import Vtp
from rest_framework import viewsets
from .serializers import VtpSerializer


class VtpViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vtp.objects.all()
    serializer_class = VtpSerializer
    http_method_names = ["get", "head"]
