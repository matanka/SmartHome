# Generated by Django 3.2.9 on 2021-11-07 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_alter_device_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
