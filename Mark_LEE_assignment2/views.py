from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse
from schedule2.models import Schedule
from schedule2.models import Customer
from schedule2.models import Booking
from django.shortcuts import render

def main(request):
  return render(request, 'main.html', {})

def search(request):
  template = loader.get_template('search.html')
  return HttpResponse(template.render({}, request))

def searched(request):
  date = request.POST['date']
  entries = Schedule.objects.filter(date=date, capacity__gt=0).values()
  template = loader.get_template('searched.html')
  context = {
    'mysearch' : entries,
  }
  return HttpResponse(template.render(context, request))

def book(request, id):
  flight = Schedule.objects.get(id=id)
  template = loader.get_template('book.html')
  context = {
    'flight' : flight,
  }
  return HttpResponse(template.render(context, request))

def addcustomer(request):
  template = loader.get_template('addcustomer.html')
  return HttpResponse(template.render({}, request))

def add_customer_detail(request):
  x = request.POST['name']
  customer = Customer(name=x)
  customer.save()
  return HttpResponseRedirect(reverse('customerList'))

def customerList(request):
  customer = Customer.objects.all().values()
  template = loader.get_template('customerlist.html')
  context = {
    'customer': customer,
  }
  return HttpResponse(template.render(context, request))

def addrecord(request, id):
  template = loader.get_template('invoice.html')
  schedule = Schedule.objects.get(id=id)
  schedule.capacity -= 1
  schedule.save()
  name = request.POST['name']
  depart = request.POST['departure']
  desti = request.POST['destination']
  flight = request.POST['flightname']
  cap = request.POST['capacity']
  date = request.POST['date']
  departtime = request.POST['departuretime']
  arrtime = request.POST['arrivaltime']
  price = request.POST['price']
  scheduleID = request.POST['scheduleID']
  booking = Booking(name=name, departure=depart, destination=desti, flightName=flight, capacity=cap, date=date, departureTime=departtime, arrivalTime=arrtime, price=price, scheduleID=scheduleID)
  booking.save()
  context = {
    'flight' : schedule,
    'booking' : booking,
  }
  return HttpResponse(template.render(context, request))

def bookedflight(request):
  booking = Booking.objects.all().values()
  template = loader.get_template('bookedflight.html')
  context = {
    'booking': booking,
  }
  return HttpResponse(template.render(context, request))

def reference(request):
  template = loader.get_template('reference.html')
  return HttpResponse(template.render({}, request))

def searchreference(request):
  reference = request.POST['reference']
  entries = Booking.objects.get(id=reference)
  template = loader.get_template('searchedreference.html')
  context = {
    'flight' : entries,
  }
  return HttpResponse(template.render(context, request))

def cancelation(request):
  return render(request, 'cancelation.html', {})

def confirmcancelation(request):
  reference = request.POST['reference']
  entries = Booking.objects.get(id=reference)
  template = loader.get_template('confirmcancelation.html')
  context = {
    'flight' : entries,
  }
  entries.delete()
  schedule = Schedule.objects.get(id=entries.scheduleID)
  schedule.capacity += 1
  schedule.save()
  return HttpResponse(template.render(context, request))

def name(request):
  return render(request, 'name.html', {})

def searchname(request):
  search = request.POST['bookedname']
  entries = Booking.objects.filter(name=search).values()
  template = loader.get_template('searchedname.html')
  context = {
    'flight' : entries,
  }
  return HttpResponse(template.render(context, request))

def searchdestination(request):
  return render(request, 'searchdestination.html', {})

def searcheddesti(request):
  search = request.POST['destination']
  entries = Schedule.objects.filter(destination=search).values()
  template = loader.get_template('searcheddesti.html')
  context = {
    'flight' : entries,
  }
  return HttpResponse(template.render(context, request))

def bookdestination(request,id):
  flight = Schedule.objects.get(id=id)
  template = loader.get_template('book.html')
  context = {
    'flight' : flight,
  }
  return HttpResponse(template.render(context, request))