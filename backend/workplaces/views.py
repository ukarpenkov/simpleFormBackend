from rest_framework import viewsets
from .models import Workplace
from .serializers import WorkplaceSerializer

class WorkplaceViewSet(viewsets.ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer
