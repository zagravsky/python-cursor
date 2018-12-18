"""mysite URL Configuration

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

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from geologysite.views import *


urlpatterns = [

    path('', HomePageView.as_view(), name='home_page'),

    path('registration/', RegistrationView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('minerals/', MineralsListView.as_view(), name='list_minerals'),
    path('minerals/<int:pk>/', MineralDetailView.as_view(), name='detail_mineral'),
    path('rocks/<str:type>/', RockListView.as_view(), name='list_rocks'),
    path('<int:pk>/', RockDetailView.as_view(), name='detail_rock',),

    path('blog/', BlogPageView.as_view(), name='blog_page'),
    path('blog/article=<int:pk>', DetailArticleView.as_view(), name='article'),
    path('blog/add', CreateArticleView.as_view(), name='create_article'),
    path('blog/update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('blog/delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),

    path('ckeditor/', include('ckeditor_uploader.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
