# Generated by Django 4.2.2 on 2023-06-30 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCentre', '0020_prescription_prescribingpatient_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='PrescribingPatient',
            new_name='prescribingPatient',
        ),
    ]
