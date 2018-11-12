from django import forms
from .models import Flowers


class NewFlowersForm(forms.ModelForm):
    class Meta:
        model = Flowers
        fields = '__all__'
