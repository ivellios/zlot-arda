# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
import settings

from zapisy.models import *
from patroni.models import Patron

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from news.views import IndexView
from patroni.views import PatroniView, SponsorzyView
from zapisy.views import LarpView

urlpatterns = patterns('',
    # Example:
    
    # (r'^arda/', include('arda.foo.urls')),
    (r'^$', IndexView.as_view()),
    (r'^news/',include('news.urls')),
    (r'^galeria/',include('galeria.urls')),
    (r'^zlot/',include('zlot.urls')),
    
    url(r'^larp/(?P<slug>[\w_-]+)?$', LarpView.as_view(), name='larp_text'),
    url(r'^frakcja/(?P<lslug>[\w_-]+)/(?P<fslug>[\w_-]+)/zapis/?$', 'zapisy.views.zapis_do_frakcji', name='frakcja_zapis'),
    url(r'^frakcja/(?P<lslug>[\w_-]+)/(?P<fslug>[\w_-]+)/?$', 'zapisy.views.show_frakcja', name='frakcja_text'),
    url(r'^konto/frakcje/lista', 'zapisy.views.show_frakcja_list', name="frakcja_list"),
    url(r'^konto/frakcje/dyskusja/(?P<frakcja_id>[\d]+)/?$', 'zapisy.views.frakcja_wpisy', name="frakcja_wpisy"),
    url(r'^rejestracja/(?P<rok>\d+)/?$','zapisy.views.nowy_zapis', name="zapisy"),
    url(r'^konto/logowanie/$', 'django.contrib.auth.views.login', {'template_name': 'zapisy/login.html'}, name = 'login'),
    
    #url(r'^konto/logowanie/', 'zapisy.views.zloty_login', name="login"),
    url(r'^konto/wylogowanie/', 'zapisy.views.zloty_logout', name="logout"),
    url(r'^konto/haslo/zmiana/', 'zapisy.views.change_password', name="password_change"),
    url(r'^konto/haslo/reset/(?P<uid>\d+)/(?P<code>\w+)/', 'zapisy.views.reset_password', name="password_reset_confirm"),
    url(r'^konto/haslo/reset/', 'zapisy.views.reset_password', name="password_reset"),

    url(r'^konto/zapis/(?P<rok>\d+)?$','zapisy.views.zapis',name="zapisy_zalogowany"),
    #url(r'^voting/(?P<hashset>[\w]+)/?$', 'zlot.views.voting', name="zlot_voting"),
    #url(r'^vote/(?P<hashset>[\w]+)/?$', 'zlot.views.vote', name="zlot_vote"),
    #url(r'^msgvotes/?$', 'zlot.views.send_votes', name="zlot_vote_send"),
    
    

    #url(r'^zapisy/lista/(?P<rok>\d+)/?$', 'zapisy.views.lista_zapisanych', name = "zapisy_lista_zapisanych"),
    #url(r'^zapisy/lista_frakcja/(?P<larp_slug>[\w_-]+)/?$', 'zapisy.views.lista_bez_frakcji', name = "zapisy_lista_bez_frakcji"),
    #url(r'^zapisy/kod/(?P<userid>\d+)/?$','zapisy.views.get_hash',name="zapisy-kod-test"),
    #url(r'^zapisy/wyslijkody/(?P<hash>\w+)/?$','zapisy.views.wyslij_kody',name="zapisy-kody"),

    
    #url(r'^zloty/$', 'zapisy.views.zloty', name="zapisy_zloty"),
    # tymczasowy tekst, gdy nie ma zapis�w
	#url(r'^zapisy/$',informacje,{'text':'zapisy'},name="zapisy"),
	#url(r'^listaWyjazdowa$',object_list,{'template_name':'listaWyjazdowa.html','queryset':Uczestnictwo.objects.filter(zlot__rok=2012)}),
    
    url(r'^partnerzy/?$', SponsorzyView.as_view(), name = 'partnerzy'),
    url(r'^patroni/?$', PatroniView.as_view(), name = 'patroni'),

    url(r'^mail/$','zapisy.views.info', ),
    #(r'^info/$','zapisy.views.infoUcz'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.ADMIN_MEDIA_PREFIX}),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
