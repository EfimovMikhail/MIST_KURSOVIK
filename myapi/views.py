from rest_framework import viewsets

from .serializers import MeropSerializer
from .models import Merop

class MeropViewSet(viewsets.ModelViewSet):
    queryset = Merop.objects.all().order_by('name')
    serializer_class = MeropSerializer
