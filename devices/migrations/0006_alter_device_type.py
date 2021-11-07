# Generated by Django 3.2.9 on 2021-11-07 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_rename_data_device_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.CharField(choices=[('a/c', 'Air Conditioner'), ('switch', 'Switch'), ('water_heater', 'Water Heater')], max_length=50),
        ),
    ]
