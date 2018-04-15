from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.contrib.auth import logout
from .models import *
from .forms import *

def home(request):
    return render(request,'hospitalmanagement.html')

def Patientlogin(request):
    if request.method == "POST":
        form = PatientLoginForm(request.POST)
        print(form.errors)
        if form.is_valid():
            Email = form.cleaned_data.get('email')
            Password = form.cleaned_data.get('password')
            patient = Patient.objects.get(email=Email,password=Password)
            # request.session["patientObject"] = patient
            if patient:
                return render(request, "PatientHomePage.html" , {'patient' : patient})
            else:
                return redirect('/patient/login')
        else:
            print("form not valid")
            return redirect(Patientlogin)
    else:
        form = PatientLoginForm()
        return render(request, "PatientLogin.html", {'form' : form})

def patientSignup(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            # email = form.cleaned_data.get('email')
            # request.session['email'] = email
            return redirect('/home')
        return redirect(patientSignup)
    else:
        form = PatientForm()
        return render(request, "PatientSignup.html", {'form' : form})

def doctorSignup(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            # email = form.cleaned_data.get('email')
            # request.session['email'] = email
            return redirect('/home')
        return redirect(doctorSignup)
    else:
        form = DoctorForm()
        return render(request, "DoctorSignup.html", {'form' : form})

def Doctorlogin(request):
    if request.method == "POST":
        form = DoctorLoginForm(request.POST)
        print(form.errors)
        if form.is_valid():
            Email = form.cleaned_data.get('email')
            Password = form.cleaned_data.get('password')
            doctor = Doctor.objects.get(email=Email,password=Password)
            # request.session["doctorObject"] = doctor
            if doctor:
                return render(request, "DoctorHomePage.html" , {'Doctor' : doctor})
            else:
                return redirect('/doctor/login')
        else:
            return redirect(Doctorlogin)
    else:
        form = DoctorLoginForm()
        return render(request, "DoctorLogin.html", {'form' : form})

def fillRecord(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        print(form.errors)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect(home)
        return redirect(fillRecord)
    else:
        form = RecordForm()
        return render(request,"FillRecord.html",{'form': form})

def viewRecord(request):
    if request.method == "POST":
        patientemail = request.POST.get("email", "")
        record = PatientRecord.objects.get(Patientid = patientemail)
        patient = Patient.objects.get(email = patientemail)
        return render(request,"RecordPage.html",{'record' : record,'patient' : patient})

def viewBill(request):
    if request.method == "POST":
        patientemail = request.POST.get("email", "")
        bill = Bill.objects.get(Patientid = patientemail)
        patient = Patient.objects.get(email = patientemail)
        return render(request,"BillPage.html",{'bill' : bill,'patient' : patient})
