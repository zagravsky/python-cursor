from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import MineralModel, RockModel
from .forms import NewMineralForm, RockForm
from django.urls import reverse


class HomePageView(TemplateView):
    template_name = 'base.html'


class MineralsListView(ListView):
    model = MineralModel
    template_name = 'minerals.html'


class MineralDetailView(DetailView):
    model = MineralModel
    template_name = 'mineral_data.html'


class NewMineralCreate(CreateView):
    model = MineralModel
    form_class = NewMineralForm
    template_name = 'create_min.html'

    def get_success_url(self):
        return reverse("detail_mineral", args=(self.object.id,))


class RockListView(ListView):
    model = RockModel
    template_name = 'rocks.html'


class RockDetailView(DetailView):
    model = RockModel
    template_name = 'rock_data.html'
