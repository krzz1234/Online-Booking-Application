# Generated by Django 4.0.4 on 2022-06-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule2', '0004_alter_booking_date_alter_schedule_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrivalTime',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='departureTime',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='arrivalTime',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='departureTime',
            field=models.CharField(max_length=255),
        ),
    ]
