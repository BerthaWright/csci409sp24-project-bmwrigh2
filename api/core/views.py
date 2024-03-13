from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from core.models import Airline, Airport, Flight, Runway
from core.serializers import AirlineSerializer, AirportSerializer, FlightSerializer, RunwaySerializer
# Create your views here.

class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class =  AirportSerializer

class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class =  AirlineSerializer
    
class RunwayViewSet(viewsets.ModelViewSet):
    queryset = Runway.objects.all()
    serializer_class =  RunwaySerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class =  FlightSerializer