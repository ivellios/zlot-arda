# -*- coding:utf-8 -*-

from patroni.models import Sponsor, Patron

from django.views.generic.list import ListView

class PatroniView(ListView):
	template_name = 'patroni/patroni_list.html'
	model = Patron

class SponsorzyView(ListView):
	template_name = 'patroni/patroni_list.html'
	model = Sponsor

