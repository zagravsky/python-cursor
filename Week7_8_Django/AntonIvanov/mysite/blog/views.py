from .models import Article
from .forms import NewArticleForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, FormView, View
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class IndexView(ListView):
    model = Article
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = "All articles"
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'add_article.html'
    form_class = NewArticleForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id, ))


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
