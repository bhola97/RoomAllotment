# Generated by Django 2.1.11 on 2020-03-21 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomBooking', '0006_auto_20200321_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='fromDate',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='guest',
            name='fromTime',
            field=models.TimeField(blank=True, default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='guest',
            name='toDate',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='guest',
            name='toTime',
            field=models.TimeField(blank=True, default=datetime.time(0, 0)),
        ),
    ]
