# Generated by Django 2.0.3 on 2018-04-14 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('BillNo', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('MedicineCharge', models.IntegerField(default=0)),
                ('RoomCharge', models.IntegerField(default=0)),
                ('LabCharge', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('Department', models.CharField(blank=True, max_length=15, null=True)),
                ('ArrivalTime', models.TimeField(null=True)),
                ('DepartureTime', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('email', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, max_length=6, null=True)),
                ('Address', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone_no', models.CharField(blank=True, max_length=12, null=True)),
                ('Doctorid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('RecordNo', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('DateOfAdmission', models.DateTimeField()),
                ('DateOfDischarge', models.DateTimeField()),
                ('Disease', models.CharField(blank=True, max_length=20, null=True)),
                ('Medicine', models.TextField()),
                ('Patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('RoomNo', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Status', models.BooleanField(default=False)),
                ('Patientid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patientrecord',
            name='RoomNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.Room'),
        ),
        migrations.AddField(
            model_name='bill',
            name='Patientid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.Patient'),
        ),
    ]