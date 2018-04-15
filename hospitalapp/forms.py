from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.admin import widgets
from .models import *

class PatientForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Patient
		fields = ['email','password','Name','Age','Gender','Address','Phone_no','Doctorid']

# class PatientLoginForm(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Patient
#         fields = ['email','password']

class PatientLoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    # class Meta:
    #     fields = ['email','password']

class DoctorForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Doctor
		fields = ['email','password','Name','Department','ArrivalTime','DepartureTime']

class DoctorLoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class RecordForm(ModelForm):
    Patientid = forms.ModelChoiceField(queryset=Patient.objects.all())
    RoomNo = forms.ModelChoiceField(queryset=Room.objects.filter(Status=False))
    Medicine = forms.CharField(widget=forms.Textarea)
    DateOfAdmission = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    DateOfDischarge = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    class Meta:
        model = PatientRecord
        fields = '__all__'
