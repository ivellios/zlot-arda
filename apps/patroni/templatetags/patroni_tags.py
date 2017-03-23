
from django import template

from patroni.models import Patron, Sponsor

register = template.Library()

@register.inclusion_tag('patroni/block_patroni.html')
def patroni_block():
    patroni = Patron.objects.all()
    return {'objects_list':patroni}
	
@register.inclusion_tag('patroni/block_sponsorzy.html')
def sponsorzy_block():
	sponsorzy = Sponsor.objects.all()
	return {'objects_list': sponsorzy}