# -*- coding: utf-8 -*-

from galeria.models import Album
from news.models import Category

def site(request):
    return {
            'galleries':Album.objects.all().order_by('-id'),
            'news_categories': Category.objects.all().order_by('name')
            }
