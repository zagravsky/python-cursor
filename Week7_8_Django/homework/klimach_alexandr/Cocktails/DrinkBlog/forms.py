from django import forms
from .models import Cocktail


class NewCocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = '__all__'
