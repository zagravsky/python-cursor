from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Post
from .forms import ComposePostForm


class IndexView(ListView):
    """
    Shows the list of posts on homepage
    """
    model = Post
    template_name = 'index.html'


class PostContentView(DetailView):
    """
    Shows the post on separate page
    """
    model = Post
    template_name = 'content.html'


class ComposePostView(CreateView):
    """
    Shows the page where user can write new post - with Title, Content and Author fields
    """
    model = Post
    template_name = 'compose.html'
    form_class = ComposePostForm

    def get_success_url(self):
        return reverse('index')


class UpdatePostView(UpdateView):
    """
    Shows the page where user can update existing post - with Title, Content and Author fields
    """
    model = Post
    template_name = "update.html"
    form_class = ComposePostForm

    def get_success_url(self):
        return reverse('content', args=(self.object.id,))


class DeletePostView(DeleteView):
    """
    Shows the confirmation when user clicks on 'delete' near the post on Content page
    """
    model = Post
    success_url = "/"
    template_name = "delete.html"
