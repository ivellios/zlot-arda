# Create your views here.
from django.views.generic import TemplateView
from static.models import *
from django.shortcuts import get_object_or_404

class StaticView(TemplateView):
    template_name = 'static/show_static.html'

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        context['static_content'] = get_object_or_404(StaticContent, slug=kwargs.get('slug'), )
        return context
