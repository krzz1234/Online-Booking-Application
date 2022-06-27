from django.db import models

class Schedule(models.Model):
	departure = models.CharField(max_length=255)
	destination = models.CharField(max_length=255)
	flightName = models.CharField(max_length=255)
	capacity = models.IntegerField()
	date = models.CharField(max_length=255)
	departureTime = models.CharField(max_length=255)
	arrivalTime = models.CharField(max_length=255)
	price = models.IntegerField()

class Customer(models.Model):
	name = models.CharField(max_length=255)
		
class Booking(models.Model):
	name = models.CharField(max_length=255)
	departure = models.CharField(max_length=255)
	destination = models.CharField(max_length=255)
	flightName = models.CharField(max_length=255)
	capacity = models.IntegerField()
	date = models.CharField(max_length=255)
	departureTime = models.CharField(max_length=255)
	arrivalTime = models.CharField(max_length=255)
	price = models.IntegerField()
	scheduleID = models.CharField(max_length=255)