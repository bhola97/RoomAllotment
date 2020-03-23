# Generated by Django 2.1.11 on 2020-03-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Occupancy', models.CharField(choices=[('S', 'Single Room'), ('D', 'Room for Two'), ('T', 'Room for Three'), ('F', 'Room for Four')], default='S', max_length=1)),
            ],
        ),
    ]
