# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

class Doctor(models.Model):
	Name = models.CharField(max_length=30, blank=True, null=True)
	email = models.CharField(primary_key=True,max_length=50,default=None)
	password = models.CharField(max_length=50,blank=True, null=True)
	Department = models.CharField(max_length=15, blank=True, null=True)
	ArrivalTime = models.TimeField(null=True)
	DepartureTime = models.TimeField(null=True)

class Patient(models.Model):
	email = models.CharField(primary_key=True,max_length=50,default=None)
	password = models.CharField(max_length=50,blank=True, null=True)
	Name = models.CharField(max_length=30, blank=True, null=True)
	Age = models.IntegerField(blank=True, null=True)
	Gender = models.CharField(max_length=6, blank=True, null=True)
	Address = models.CharField(max_length=50, blank=True, null=True)
	Phone_no = models.CharField(max_length=12,blank=True, null=True)
	Doctorid = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)

class Room(models.Model):
	RoomNo = models.AutoField(primary_key=True,default=None)
	Status = models.BooleanField(default=False)
	Patientid = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True,blank=True)

class PatientRecord(models.Model):
	RecordNo = models.AutoField(primary_key=True,default=None)
	Patientid = models.ForeignKey(Patient,on_delete=models.CASCADE)
	DateOfAdmission = models.DateField()
	DateOfDischarge = models.DateField()
	RoomNo = models.ForeignKey(Room,on_delete=models.CASCADE)
	Disease = models.CharField(max_length=20, blank=True, null=True)
	Medicine = models.TextField()

class Bill(models.Model):
	BillNo = models.AutoField(primary_key=True,default=None)
	Patientid = models.ForeignKey(Patient,on_delete=models.CASCADE)
	MedicineCharge = models.IntegerField(default=0)
	RoomCharge = models.IntegerField(default=0)
	LabCharge = models.IntegerField(default=0)
	#TotalBill = models.IntegerField()
	@property
	def TotalBill(self):
		return self.MedicineCharge + self.RoomCharge + self.LabCharge
