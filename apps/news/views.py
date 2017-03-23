# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from news.models import *
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

class EntryView(TemplateView):
    template_name = 'news/single.html'

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        context['news'] = get_object_or_404(News, slug=kwargs.get('slug'), )
        return context

class IndexView(ListView):
    template_name = 'news/index.html'
    queryset = News.objects.all().order_by('-id')[:3]

class ArchiveView(ListView):
    template_name = 'news/list.html'
    model = News
    paginate_by = 5
