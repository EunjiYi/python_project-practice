from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):

    if request.method == "POST":
        # DB에 저장
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save() #모델 form이기 때문에 바로 save가능
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def detail(request, id):
    article = Article.objects.get(pk=id)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html',context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST,  request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    #print(form)
    context = {
        'form': form,
    }
    return render(request, 'articles/edit.html', context)


def delete(request, pk):
    data = Article.objects.get(pk=pk)
    data.delete()
    return redirect('articles:index')