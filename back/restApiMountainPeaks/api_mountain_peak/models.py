from django.db import models

class mountain_peak(models.Model):
    name = models.CharField("Name", max_length=240)
    location = models.CharField("Location", max_length=240)
    latitude = models.CharField("Latitude", max_length=240)
    longitude = models.CharField("Longitude", max_length=240)
    altitude = models.IntegerField("Altitude", max_length=240)

    def __str__(self):
        return self.name