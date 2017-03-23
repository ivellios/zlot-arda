# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from views import AlbumView

urlpatterns = patterns('galeria.views',
		url(r'^(?P<slug>[\w\-_]+)/$', AlbumView.as_view() ,name="galeria_album"),
		#(r'^$', 'showGaleria'),
)