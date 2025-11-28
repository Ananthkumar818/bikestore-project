from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Bike

def bike_list(request):
    bikes = Bike.objects.all()
    return render(request, 'bike_list.html', {'bikes': bikes})

def bike_detail(request, slug):
    bike = get_object_or_404(Bike, slug=slug)
    return render(request, 'bike_detail.html', {'bike': bike})


# Create your views here.
