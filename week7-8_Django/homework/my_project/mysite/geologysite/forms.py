from django import forms
from .models import Article, MineralModel, RockModel


class NewMineralForm(forms.ModelForm):
    class Meta:
        model = MineralModel
        fields = '__all__'


class RockForm(forms.ModelForm):
    class Meta:
        model = RockModel
        fields = '__all__'


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']
