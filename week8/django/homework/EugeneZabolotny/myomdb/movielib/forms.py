from django import forms

from .models import Movie


class NewMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
