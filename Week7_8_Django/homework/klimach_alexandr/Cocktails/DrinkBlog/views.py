from django.shortcuts import reverse
from .models import Cocktail
from .forms import NewCocktailForm
from django.views.generic import ListView, DetailView, CreateView


class CocktailListView(ListView):
    model = Cocktail
    template_name = 'index.html'


class CocktailDetailView(DetailView):
    model = Cocktail
    template_name = 'detail.html'


class CocktailCreateView(CreateView):
    model = Cocktail
    template_name = 'create.html'
    form_class = NewCocktailForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))
