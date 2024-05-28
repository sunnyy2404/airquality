from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render
from django.http import HttpResponse
from .models import infoModel
from .forms import infoForm
import pickle
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
def home(request):
    return render(request,'home.html',{})
def welcome(request):
    return render(request,'welcome.html',{})
def dataset(request):
    return render(request,'dataset.html',{})
def models(request):
    return render(request,'models.html',{})
def algorithms(request):
    return render(request,'algorithms.html',{})
def selectalgo(request):
    return render(request,'selectalgo.html',{})
def display(request):
    form=infoForm()
    if request.method=="POST":
            form=infoForm(request.POST)
            pm25=request.POST.get('pm25')
            pm10=request.POST.get('pm10')
            no=request.POST.get('no')
            no2=request.POST.get('no2')
            nox=request.POST.get('nox')
            co=request.POST.get('co')
            so2=request.POST.get('so2')
            f=infoModel(pm25=pm25,pm10=pm10,no=no,no2=no2,nox=nox,co=co,so2=so2)
            f.save()
            return HttpResponseRedirect('../displaypred')
    return render(request,'display.html',{'form1':form})
def rfrinput(request):
    form=infoForm()
    if request.method=="POST":
            form=infoForm(request.POST)
            pm25=request.POST.get('pm25')
            pm10=request.POST.get('pm10')
            no=request.POST.get('no')
            no2=request.POST.get('no2')
            nox=request.POST.get('nox')
            co=request.POST.get('co')
            so2=request.POST.get('so2')
            f=infoModel(pm25=pm25,pm10=pm10,no=no,no2=no2,nox=nox,co=co,so2=so2)
            f.save()
            return HttpResponseRedirect('../rfr')
    return render(request,'rfrinput.html',{'form1':form})
def dtrinput(request):
    form=infoForm()
    if request.method=="POST":
            form=infoForm(request.POST)
            pm25=request.POST.get('pm25')
            pm10=request.POST.get('pm10')
            no=request.POST.get('no')
            no2=request.POST.get('no2')
            nox=request.POST.get('nox')
            co=request.POST.get('co')
            so2=request.POST.get('so2')
            f=infoModel(pm25=pm25,pm10=pm10,no=no,no2=no2,nox=nox,co=co,so2=so2)
            f.save()
            return HttpResponseRedirect('../dtr')
    return render(request,'dtrinput.html',{'form1':form})
def xgb_pred(pm25,pm10,no,no2,nox,co,so2):
    with open('XGBoost.pkl','rb') as f:
        mp=pickle.load(f)
    prediction = mp.predict([[pm25,pm10,no,no2,nox,co,so2]])
    if prediction[0]<=50 and prediction[0]>0:
        return 'Good'
    elif prediction[0]<=100 and prediction[0]>50:
        return 'Moderate'
    elif prediction[0]<=150 and prediction[0]>100:
        return 'Sensitive Groups'
    elif prediction[0]<=200 and prediction[0]>151:
        return 'Unhealthy'
    elif prediction[0]<=300 and prediction[0]>201:
        return 'Very Unhealthy'
    elif prediction[0]>301:
        return 'Hazardous'
    else:
        return 'Error'
def rfr_pred(pm25,pm10,no,no2,nox,co,so2):
    with open('RandomForest.pkl','rb') as f:
        mp=pickle.load(f)
    prediction = mp.predict([[pm25,pm10,no,no2,nox,co,so2]])
    if prediction[0]<=50 and prediction[0]>0:
        return 'Good'
    elif prediction[0]<=100 and prediction[0]>50:
        return 'Moderate'
    elif prediction[0]<=150 and prediction[0]>100:
        return 'Sensitive Groups'
    elif prediction[0]<=200 and prediction[0]>151:
        return 'Unhealthy'
    elif prediction[0]<=300 and prediction[0]>201:
        return 'Very Unhealthy'
    elif prediction[0]>301:
        return 'Hazardous'
    else:
        return 'Error'
def dtr_pred(pm25,pm10,no,no2,nox,co,so2):
    with open('Decisiontree.pkl','rb') as f:
        mp=pickle.load(f)
    prediction = mp.predict([[pm25,pm10,no,no2,nox,co,so2]])
    if prediction[0]<=50 and prediction[0]>0:
        return 'Good'
    elif prediction[0]<=100 and prediction[0]>50:
        return 'Moderate'
    elif prediction[0]<=150 and prediction[0]>100:
        return 'Sensitive Groups'
    elif prediction[0]<=200 and prediction[0]>151:
        return 'Unhealthy'
    elif prediction[0]<=300 and prediction[0]>201:
        return 'Very Unhealthy'
    elif prediction[0]>301:
        return 'Hazardous'
    else:
        return 'Error'
def displaypred(request):
    obj=infoModel.objects.last()
    result=xgb_pred(obj.pm25,obj.pm10,obj.no,obj.no2,obj.nox,obj.co,obj.so2)
    return render(request,'displaypred.html',{'object':result,'val':obj})
def rfr(request):
    obj=infoModel.objects.last()
    result=rfr_pred(obj.pm25,obj.pm10,obj.no,obj.no2,obj.nox,obj.co,obj.so2)
    return render(request,'rfr.html',{'object':result,'val':obj})
def dtr(request):
    obj=infoModel.objects.last()
    result=dtr_pred(obj.pm25,obj.pm10,obj.no,obj.no2,obj.nox,obj.co,obj.so2)
    return render(request,'dtr.html',{'object':result,'val':obj})
    