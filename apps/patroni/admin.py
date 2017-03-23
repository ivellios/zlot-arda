# -*- coding:utf-8 -*-
from models import *

from django.contrib import admin

class PatronAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kolejnosc']
    
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kolejnosc']

admin.site.register(Patron, PatronAdmin)
admin.site.register(Sponsor, SponsorAdmin)
