"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from todolist.views import IndexView, TodoDetailView, TodoAddView, TodoUpdate, TodoDelete, LoginFormView, LogoutView, \
    HomeView, RegisterView, ProfileView, EditProfileView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('todos/details/<int:pk>', TodoDetailView.as_view(), name='details'),
    path('todos/add/', TodoAddView.as_view(), name='add'),
    path('admin/', admin.site.urls),
    path('todos/details/<int:pk>/upd', TodoUpdate.as_view(), name='todoupdate'),
    path('todos/<int:pk>/delete', TodoDelete.as_view(), name='tododelete'),

    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('accounts/register/', RegisterView.as_view(), name="register"),
    path('accounts/profile/', ProfileView.as_view(), name="profile"),
    path('accounts/profile/edit/', EditProfileView.as_view(), name="edit_profile"),


] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) +\
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
