from django.shortcuts import render
from rest_framework import viewsets
from core.models import Vessel, BillOfLanding, Container, VesselSchedule
from core.serializers import VesselSerializer, BillOfLandingSerializer, VesselScheduleSerializer, ContainerSerializer
# Create your views here.

class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class =  VesselSerializer

class VesselScheduleViewSet(viewsets.ModelViewSet):
    queryset = VesselSchedule.objects.all()
    serializer_class =  VesselScheduleSerializer
    
class BillOfLandingViewSet(viewsets.ModelViewSet):
    queryset = BillOfLanding.objects.all()
    serializer_class =  BillOfLandingSerializer
    
    
class ContainerViewSet(viewsets.ModelViewSet):
   queryset = Container.objects.all()
   serializer_class = ContainerSerializer
