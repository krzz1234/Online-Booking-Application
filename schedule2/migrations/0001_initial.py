# Generated by Django 4.0.4 on 2022-06-01 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('flightName', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('date', models.DateField()),
                ('departureTime', models.TimeField()),
                ('arrivalTime', models.TimeField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
