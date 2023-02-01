from django.conf import settings
from django.contrib.gis.db import models


class Culture(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return  self.name


class Farmer(models.Model):
    full_name = models.CharField(max_length=50)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.full_name


class Season(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return  self.name


class Plot(models.Model):
    contour = models.PolygonField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
