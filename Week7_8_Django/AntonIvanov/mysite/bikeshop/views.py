from .models import Bike
from .forms import NewBikeForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse


class IndexView(ListView):
    model = Bike
    template_name = 'index.html'


class BikeDetailView(DetailView):
    model = Bike
    template_name = "detail.html"


class BikeCreateView(CreateView):
    model = Bike
    template_name = "add_bike.html"
    form_class = NewBikeForm

    def get_success_url(self):
        return reverse('detail',args=(self.object.id, ))
