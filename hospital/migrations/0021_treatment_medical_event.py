# Generated by Django 3.0.5 on 2023-11-25 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_auto_20231125_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='medical_event',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.MedicalEvent'),
        ),
    ]
