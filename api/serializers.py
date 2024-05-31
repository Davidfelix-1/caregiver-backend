from rest_framework import serializers
from .models import User, Service, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_caregiver', 'is_senior']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description']

class AppointmentSerializer(serializers.ModelSerializer):
    caregiver = UserSerializer()
    senior = UserSerializer()
    service = ServiceSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'caregiver', 'senior', 'service', 'date', 'notes']