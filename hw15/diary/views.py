from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from .models import Post
from .forms import ComposePostForm



class Index(ListView):
    model = Post
    template_name = 'index.html'


class Content(DetailView):
    model = Post
    template_name = 'content.html'


class Compose(CreateView):
    model = Post
    template_name = 'compose.html'
    form_class = ComposePostForm

    def get_success_url(self):
        return reverse('index')
