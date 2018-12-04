from django.shortcuts import render
# from django.http import HttpResponse
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})
