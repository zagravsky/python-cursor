from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewTodoForm
from .models import Todo


class IndexView(ListView):
    model = Todo
    template_name = 'index.html'


class HomeView(ListView):
    model = Todo
    template_name = 'home.html'


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'details.html'


class TodoAddView(CreateView):
    model = Todo
    template_name = 'add.html'
    form_class = NewTodoForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TodoAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('details', args=(self.object.id,))


class TodoUpdate(UpdateView):
    model = Todo
    form_class = NewTodoForm
    template_name = 'todoupd.html'

    def form_valid(self, form):
        form.instance.create_at = timezone.now()
        return super(TodoUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('details', args=(self.object.id,))


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('home')


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
