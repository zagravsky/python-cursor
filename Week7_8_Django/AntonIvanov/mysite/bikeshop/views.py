from django.shortcuts import render, get_object_or_404, redirect
from .models import Bike
from .forms import NewBikeForm
from django.views.generic import ListView, DetailView, CreateView


def index(request):
    bikes = Bike.objects.all()
    return render(request, 'index.html', {'bikes': bikes})

# one bike
def detail(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    return render(request, 'detail.html', {'bike': bike})



def add_bike(request):
    if request.POST:
        form = NewBikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewBikeForm()
    return render(request, 'add_bike.html', {'form': form})
