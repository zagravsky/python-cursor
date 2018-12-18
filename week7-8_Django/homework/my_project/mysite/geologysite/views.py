from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from .models import MineralModel, RockModel, Article
from .forms import ArticleForm


# ---------------------------------------
# Generic view for geological data
# ---------------------------------------


class HomePageView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_articles'] = Article.objects.order_by('-date_publication')[:4]
        return context


class MineralsListView(ListView):
    model = MineralModel
    template_name = 'minerals.html'


class MineralDetailView(DetailView):
    model = MineralModel
    template_name = 'mineral_data.html'


class RockListView(ListView):
    model = RockModel
    template_name = 'rocks.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(type__contains=self.kwargs['type'])


class RockDetailView(DetailView):
    model = RockModel
    template_name = 'rock_data.html'


# ----------------------------------------------------
# Next part of view contain all generic view for blog
# ----------------------------------------------------


class BlogPageView(ListView):
    model = Article
    template_name = "blog_templates/articles_list.html"


class DetailArticleView(DetailView):
    model = Article
    template_name = "blog_templates/article.html"


class CreateArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog_templates/add_article.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article', args=(self.object.id,))


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog_templates/update.html'

    def get_object(self, *args, **kwargs):
        obj = super(ArticleUpdateView, self).get_object(*args, **kwargs)
        if not self.request.user.is_authenticated:
            raise PermissionError()
        return obj

    def get_success_url(self):
        return reverse('article', args=(self.object.id,))


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog_templates/modules/confirm_delete.html'

    def get_object(self, *args, **kwargs):
        obj = super(ArticleDeleteView, self).get_object(*args, **kwargs)
        if not self.request.user.is_authenticated:
            raise PermissionError
        return obj

    def get_success_url(self):
        return reverse('blog_page')

# --------------------------------------------------
# Generic view for registration
# --------------------------------------------------


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)
