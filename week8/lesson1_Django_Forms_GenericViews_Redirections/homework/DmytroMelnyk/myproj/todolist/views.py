from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewTodoForm
from .models import Todo


class IndexView(ListView):
    model = Todo
    template_name = 'index.html'


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'details.html'


class TodoAddView(CreateView):
    model = Todo
    template_name = 'add.html'
    form_class = NewTodoForm

    def get_success_url(self):
        return reverse('details', args=(self.object.id,))
