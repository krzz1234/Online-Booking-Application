# Generated by Django 4.0.4 on 2022-06-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule2', '0005_alter_booking_arrivaltime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='scheduleID',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]