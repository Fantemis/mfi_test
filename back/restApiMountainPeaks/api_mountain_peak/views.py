from django.shortcuts import render

from django.shortcuts import render
from .models import mountain_peak
from rest_framework import generics
from .serializers import MountainPeakSerializer


class MountainPeakCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new mountain peak
    queryset = mountain_peak.objects.all(),
    serializer_class = MountainPeakSerializer


class MountainPeakList(generics.ListAPIView):
    # API endpoint that allows mountain peak to be viewed.
    queryset = mountain_peak.objects.all()
    serializer_class = MountainPeakSerializer

class MountainPeakUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a mountain peak record to be updated.
    queryset = mountain_peak.objects.all()
    serializer_class = MountainPeakSerializer

class MountainPeakDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a mountain peak record to be deleted.
    queryset = mountain_peak.objects.all()
    serializer_class = MountainPeakSerializer

class MountainPeakDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single mountain peak by pk.
    queryset = mountain_peak.objects.all()
    serializer_class = MountainPeakSerializer