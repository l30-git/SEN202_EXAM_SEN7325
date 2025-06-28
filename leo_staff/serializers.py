from rest_framework import serializers
from .models import Staff, Manager, Intern

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class ManagerSerializer(StaffSerializer):
    class Meta(StaffSerializer.Meta):
        model = Manager

class InternSerializer(StaffSerializer):
    class Meta(StaffSerializer.Meta):
        model = Intern

