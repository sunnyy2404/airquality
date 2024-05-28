from django.db import models

# Create your models here.

class infoModel(models.Model):
    pm25=models.FloatField()
    pm10=models.FloatField()
    no=models.FloatField()
    no2=models.FloatField()
    nox=models.FloatField()
    co=models.FloatField()
    so2=models.FloatField()
