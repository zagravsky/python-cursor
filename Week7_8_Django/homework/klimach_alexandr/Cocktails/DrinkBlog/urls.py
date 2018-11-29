from django.urls import path
from .views import CocktailListView, CocktailDetailView, CocktailCreateView

urlpatterns = [
    path('', CocktailListView.as_view(), name='index'),
    path('<int:pk>', CocktailDetailView.as_view(), name='detail'),
    path('create', CocktailCreateView.as_view(), name='create')
]