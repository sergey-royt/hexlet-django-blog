from django.views.generic.base import TemplateView, View
# Create your views here.
from hexlet_django_blog.article.models import Article, ArticleComment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleCommentForm, ArticlesForm
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'article'
        return context

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(TemplateView):
    template_name = "articles/article.html"


    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        comments = ArticleComment.objects.all()
        return render(request, 'articles/article.html', context={
            'article': article,
        })


class ArticleCommentsView(TemplateView):

    def get(self, request, *args, **kwargs):
        comments = get_object_or_404(ArticleComment, article_id=kwargs['article_id'])

        return render(request, 'articles/comments.html', context={
            'comments': comments
        })


class ArticleCommentFormView(View):

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            form.save()


class ArticlesCreateView(View):
    template_name = 'articles/create.html'
    def get(self, request, *args, **kwargs):
        form = ArticlesForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Cтатья успешно добавлена!")
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticlesForm(instance=article)
        return render(request, 'articles/edit.html', {'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticlesForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Статья успешно отредактирована')
            return redirect('articles')

        messages.add_message(request, messages.ERROR, 'Исправьте следующие поля:')
        return render(request, 'articles/edit.html', {'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.add_message(request, messages.SUCCESS, 'Статья успешно удалена')
        return redirect('articles')
