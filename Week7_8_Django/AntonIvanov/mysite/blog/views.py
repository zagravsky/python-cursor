# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Article
from .forms import NewArticleForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse


class IndexView(ListView):
    model = Article
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'add_article.html'
    form_class = NewArticleForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id, ))

# def detail(request, article_id):
#     article = get_object_or_404(Article, pk=article_id)
#     return render(request, 'detail.html', {'article': article})

# def add_article(request):
#     if request.POST:
#         form = NewArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = NewArticleForm()
#     return render(request, 'add_article.html', {'form': form})
