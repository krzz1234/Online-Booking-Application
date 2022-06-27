from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Schedule
from .models import Customer

def index(request):
  schedule = Schedule.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'schedule': schedule,
  }
  return HttpResponse(template.render(context, request))

def customerList(request):
  customer = Customer.objects.all().values()
  template = loader.get_template('customerlist.html')
  context = {
    'customer': customer,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  depart = request.POST['departure']
  desti = request.POST['destination']
  flight = request.POST['flightname']
  cap = request.POST['capacity']
  date = request.POST['date']
  departtime = request.POST['departuretime']
  arrtime = request.POST['arrivaltime']
  price = request.POST['price']
  schedule = Schedule(departure=depart, destination=desti, flightName=flight, capacity=cap, date=date, departureTime=departtime, arrivalTime=arrtime, price=price)
  schedule.save()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  schedule = Schedule.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'schedule': schedule,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  depart = request.POST['departure']
  desti = request.POST['destination']
  flight = request.POST['flightname']
  cap = request.POST['capacity']
  date = request.POST['date']
  departtime = request.POST['departuretime']
  arrtime = request.POST['arrivaltime']
  price = request.POST['price']
  schedule = Schedule.objects.get(id=id)
  schedule.departure = depart
  schedule.destination = desti
  schedule.flightName = flight
  schedule.capacity = cap
  schedule.date = date
  schedule.departureTime = departtime
  schedule.arrivalTime = arrtime
  schedule.price = price
  schedule.save()
  return HttpResponseRedirect(reverse('index'))


def addcustomer(request):
  template = loader.get_template('addcustomer.html')
  return HttpResponse(template.render({}, request))

