from django.shortcuts import render, get_object_or_404
from .models import Bike


def index(request):
    bikes = Bike.objects.all()
    return render(request, 'index.html', {'bikes': bikes})


def detail(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    return render(request, 'detail.html', {'bike': bike})
