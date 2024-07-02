from django.forms import ModelForm
from .models import ArticleComment, Article


class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['name', 'content']


class ArticlesForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
