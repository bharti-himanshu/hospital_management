from django.contrib import admin
from hospitalapp.models import Doctor
from hospitalapp.models import Patient
from hospitalapp.models import Room
from hospitalapp.models import PatientRecord
from hospitalapp.models import Bill
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Room)
admin.site.register(PatientRecord)
admin.site.register(Bill)
# Register your models here.
