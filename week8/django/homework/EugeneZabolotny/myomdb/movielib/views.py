from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from .models import Movie
from .forms import NewMovieForm


class IndexView(ListView):
    model = Movie
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'Home | MyOMDB'
        return context


class MovieDetailedView(DetailView):
    model = Movie
    template_name = 'movie.html'


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'add_movie.html'
    form_class = NewMovieForm

    def get_success_url(self):
        return reverse('movie-detailed', args=(self.object.id,))
