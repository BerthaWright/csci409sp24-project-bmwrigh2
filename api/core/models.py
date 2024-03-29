from django.db import models

# Create your models here.
class Vessel(models.Model):
    vessel_name = models.CharField(max_length=200)

    def __str__(self):
        return self.vessel_name
    
class VesselSchedule(models.Model):
    vessel = models.ForeignKey(Vessel, on_delete = models.RESTRICT)
    voyage_number = models.CharField(max_length=50)
    arrival_date = models.DateTimeField()

    def __str__(self):
        return f'{self.vessel}-{self.voyage_number}'
    
class BillOfLanding(models.Model):
   release_designation= { 
        "C" : "Customs Hold",
        "S" : "Steamship Hold",
        "R" : "Released",
        "A" : "Available for Pickup",
   }
   voyage = models.ForeignKey(Vessel, on_delete = models.RESTRICT)
   bol_number = models.CharField(max_length=200)
   contact_name = models.CharField(max_length=200)
   contact_number = models.CharField(max_length=200)
   contact_email = models.CharField(max_length=200)
   release_status = models.CharField(max_length = 1, choices = release_designation)

   def __str__(self):
       return self.bol_number
   
class Container(models.Model):
    bol = models.ForeignKey(BillOfLanding, on_delete = models.RESTRICT)
    container_number = models.CharField(max_length=200)
    