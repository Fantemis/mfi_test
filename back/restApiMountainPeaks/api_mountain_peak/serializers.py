from rest_framework import serializers
from .models import mountain_peak

class MountainPeakSerializer(serializers.ModelSerializer):

    class Meta:
        model = mountain_peak 
        fields = ['pk', 'name', 'location', 'latitude', 'longitude', 'altitude']