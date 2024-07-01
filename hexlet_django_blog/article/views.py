from django.views.generic.base import TemplateView
# Create your views here.
from hexlet_django_blog.article.models import Article
from django.shortcuts import render, get_object_or_404

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
        return render(request, 'articles/article.html', context={
            'article': article,
        })


class ArticleCommentsView(TemplateView):

    def get(self, request, *args, **kwargs):
        comments = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])

        return render(request, 'articles/comments.html', context={
            'comments': comments
        })
