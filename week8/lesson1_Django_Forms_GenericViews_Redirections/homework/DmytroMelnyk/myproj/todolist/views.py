from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewTodoForm, RegisterForm, ProfileForm
from .models import Todo, Profile


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
    template_name = 'todo_confirm_delete.html'
    model = Todo
    success_url = reverse_lazy('home')


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                self.create_new_user(form)
                messages.success(request, "You have already register successfully!")
                return redirect(reverse("login"))

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def create_new_user(self, form):
        email = None
        if 'email' in form.cleaned_data:
            email = form.cleaned_data['email']
        User.objects.create_user(form.cleaned_data['username'], email, form.cleaned_data['password'],
                                 first_name=form.cleaned_data['first_name'],
                                 last_name=form.cleaned_data['last_name'])


class ProfileView(TemplateView):
    template_name = "registration/profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            return redirect(reverse("edit_profile"))
        context = {
            'selected_user': request.user
        }
        return render(request, self.template_name, context)


class EditProfileView(TemplateView):
    template_name = "registration/edit_profile.html"

    def dispatch(self, request, *args, **kwargs):
        form = ProfileForm(instance=self.get_profile(request.user))
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=self.get_profile(request.user))
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, "Profile update successfully!")
                return redirect(reverse("profile"))
        return render(request, self.template_name, {'form': form})

    def get_profile(self, user):
        try:
            return user.profile
        except:
            return None
