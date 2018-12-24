from django.shortcuts import render, get_object_or_404
from .models import Bike


def index(request):
    bikes = Bike.objects.all()
    return render(request, 'index.html', {'bikes': bikes})


def detail(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    return render(request, 'detail.html', {'bike': bike})


def add_bike(request):
    if request.POST:
        Bike.objects.create(
            name=request.POST.get('name'),
            brand=request.POST.get('brand'),
            bike_type=request.POST.get('bike_type'),
            wheel_size=request.POST.get('wheel_size'),
        )
    return render(request, 'add_bike.html')
