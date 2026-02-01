from rest_framework import viewsets
from .models import Certificate
from .serializers import CertificateSerializer

class CertificateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return Certificate.objects.filter(user=self.request.user)
