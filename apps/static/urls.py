from django.conf.urls.defaults import *

from views import StaticView

urlpatterns = patterns('static.views',
	(r'^(?P<slug>[\w\-_]+)/$', StaticView.as_view(), name="static_view"),
)