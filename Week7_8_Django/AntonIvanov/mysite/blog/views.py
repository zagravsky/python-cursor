from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Article
from .forms import NewArticleForm


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail.html', {'article': article})


def add_article(request):
    if request.POST:
        form = NewArticleForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect
    else:
        form = NewArticleForm()
    return render(request, 'add_article.html', {'form': form})
