"""
Tests for models.
"""

from django.test import TestCase

from core import models

from datetime import datetime

def create_vessel():
    return models.Vessel.objects.create(
        vessel_name = "Alaskan Voyager",
)    

class ModelTests(TestCase):

    def test_create_vessel(self):
        """Test Creating a vessel is Successful."""
        vessel = models.Vessel.objects.create(
           vessel_name = "Alaskan Voyager",
        )

        self.assertEqual(str(vessel), vessel.vessel_name)

    
    def test_create_vesselschedule(self):
        """Test Creating a vessel schedule is Successful."""
        vesselschedule = models.VesselSchedule.objects.create(
            vessel= create_vessel(),
            voyage_number= 12345,
            arrival_date=datetime.now(),
        )

        vesselschedule_result = str(vesselschedule.vessel) + '-' + str(vesselschedule.voyage_number)
    
        self.assertEqual(str(vesselschedule), vesselschedule_result)

#here
    def test_create_billoflanding(self):
        """Test Creating a Bill of landing is Successful."""
        billoflanding = models.BillOfLanding.objects.create(
            voyage=create_vessel(),
            bol_number = "14328",
            contact_name="John Smith",
            contact_number = 8435679000,
            contact_email="js@av.com",
            release_status = "R",
        )
        
        self.assertEqual(str(billoflanding), billoflanding.bol_number)

    def test_create_container(self):
        """Test Creating a container is Successful."""
        billoland= models.BillOfLanding.objects.create(
            voyage=create_vessel(),
            bol_number = "14328",
            contact_name="John Smith",
            contact_number = 8435679000,
            contact_email="js@av.com",
            release_status = "R",
        )
        container = models.Container.objects.create(
            bol= billoland,
            container_number= 58439058
        )
