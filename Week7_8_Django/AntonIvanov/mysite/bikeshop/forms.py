from django import forms
from .models import Bike


class NewBikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'
