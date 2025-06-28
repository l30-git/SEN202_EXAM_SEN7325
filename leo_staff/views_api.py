from rest_framework import viewsets
from .models import Staff, Manager, Intern
from .serializers import StaffSerializer, ManagerSerializer, InternSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class InternViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

