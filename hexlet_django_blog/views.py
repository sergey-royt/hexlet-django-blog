from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy('article', kwargs={'tags': 'python', 'article_id': '42'}))


def about(request):
    return render(request, 'about.html')