# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from views import EntryView, IndexView, ArchiveView

#from django.views.generic.list_detail import object_list

urlpatterns = patterns('news.views',
		url(r'^archiwum/?$', ArchiveView.as_view(), name='news_archive'),
        #url(r'^kategoria/(?P<slug>[\w\-_]+)/$', 'news_by_category',name="news-by-category"),
		url(r'^(?P<slug>[\w\-_]+)/$', EntryView.as_view(),name="news_single"),
		url(r'^$', IndexView.as_view(),name="news_index"),        
)