from django.shortcuts import render
from .models import Article
from .forms import ArticleModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def article_index(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'article-list.html', { 'articles' : articles })


def article_single(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'article-single.html', { 'article' : article })

@login_required(login_url='/auth/signin/')
def article_add(request):
    if request.method == "POST":
        form = ArticleModelForm(request.POST, request.FILES)
        if form.is_valid():
            prepared = form.save(commit=False)
            prepared.poster = request.user
            if request.FILES.get('cover', None):
                prepared.cover = request.FILES['cover']
            prepared.save()
            form = ArticleModelForm(None)
            messages.success(request, "New article has been successfully added")
    else:
        form = ArticleModelForm(None)

    return render(request, 'article-input.html', { 'form' : form, 'article' : None })

@login_required(login_url='/auth/signin/')
def article_edit(request, slug):
    article = Article.objects.get(slug=slug)

    if request.method == "POST":
        form = ArticleModelForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            prepared = form.save(commit=False)
            prepared.poster = request.user
            if request.FILES.get('cover', None):
                prepared.cover = request.FILES['cover']
            prepared.save()
            article = Article.objects.get(slug=slug)
            form = ArticleModelForm(instance=article)
            messages.success(request, "Article has been successfully updated")
    else:
        form = ArticleModelForm(instance=article)
        
    return render(request, 'article-input.html', { 'form' : form, 'article' : article })