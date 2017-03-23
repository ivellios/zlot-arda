# -*- coding: utf-8 -*-
#from django.template import RequestContext
#from django.shortcuts import render_to_response
#from django.views.generic.list_detail import object_list

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from galeria.models import *



class AlbumView(TemplateView):
    template_name = 'galeria/showAlbum.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)
        a = get_object_or_404(Album, slug=kwargs.get('slug'))
        images = a.obrazek_set.all()
        context['obrazki'] = images
        context['album'] = a

class GaleriaView(TemplateView):
    template_name = 'galeria/showGaleria.html'

    def get_context_data(self, **kwargs):
        context = super(GaleriaView, self).get_context_data(**kwargs)
        albumy = Album.objects.all().order_by('-id')
        context['albumy'] = albumy
