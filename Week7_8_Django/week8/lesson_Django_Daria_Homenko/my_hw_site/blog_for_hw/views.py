from blog_for_hw.models import Flowers
from .forms import NewFlowersForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
# # Create your views here.


class IndexView(ListView):
    model = Flowers
    template_name = "list_of_flower.html"


class FlowerDetailView(DetailView):
    model = Flowers
    template_name = "flower.html"


class FlowerCreationView(CreateView):
    model = Flowers
    template_name = "add_flower.html"
    form_class = NewFlowersForm

    def get_success_url(self):
        return reverse('flower', args=[self.object.id])

