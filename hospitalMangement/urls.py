from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='Home'),
    path('patient/signup/', views.patientSignup, name='patientSignup'),
    path('patient/login/', views.Patientlogin, name='Patientlogin'),
    path('doctor/signup/', views.doctorSignup, name='doctorSignup'),
    path('doctor/login/', views.Doctorlogin, name='Doctorlogin'),
    path('doctor/fillpatientrecord/', views.fillRecord, name='fillRecord'),
    path('patient/Record/', views.viewRecord, name='viewRecord'),
    path('patient/Bill/', views.viewBill, name='viewBill'),
    # path('patient/takeAppointment/', views.takeAppointment, name='takeAppointment'),

]
