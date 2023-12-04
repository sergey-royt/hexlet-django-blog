from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'articles/index.html', context={'name': 'articles'})


def index(request, tags, article_id):
    return HttpResponse('Статья номер ' + article_id + '. Тег ' + tags)
