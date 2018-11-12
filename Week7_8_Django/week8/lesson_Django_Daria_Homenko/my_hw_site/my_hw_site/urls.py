"""my_hw_site URL Configuration
"""
from django.contrib import admin
from django.urls import path

from blog_for_hw.views import IndexView, FlowerDetailView, FlowerCreationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('flower/<int:pk>', FlowerDetailView.as_view(), name='flower'),
    path('flower/add', FlowerCreationView.as_view(), name='flower_add')
]


