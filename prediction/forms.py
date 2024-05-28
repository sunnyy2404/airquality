from django import forms
from .models import infoModel

class infoForm(forms.Form):
    pm25=forms.FloatField()
    pm10=forms.FloatField()
    no=forms.FloatField()
    no2=forms.FloatField()
    nox=forms.FloatField()
    co=forms.FloatField()
    so2=forms.FloatField()