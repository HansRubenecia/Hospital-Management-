# Generated by Django 3.0.5 on 2023-11-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0023_remove_treatment_treatmentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
