# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('zlot.views',
		url(r'^$','informacje',name="o_zlocie"),
		#url(r'^informacje','informacje',{'text':"informacje"},name="informacje"),
		#url(r'^o-nas$','informacje',{'text':"o-nas"},name="o-nas"),
		#url(r'^plemiona','plemiona',name="plemiona"),
		url(r'^dokumenty','dokumenty',name="dokumenty"),
		url(r'^kto-jedzie','ktojedzie',name="kto_jedzie"),
		url(r'^(?P<text>[\w_-]+)/?$','informacje', name="zlot_text"),
)