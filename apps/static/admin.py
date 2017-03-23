# -*- coding: utf-8 -*-

from django.contrib import admin

from static.models import *
from common import TINY_MCE_TEXTAREAS

class StaticContentAdmin(admin.ModelAdmin):
	list_display = ('title',)
	prepopulated_fields = {'slug': ('title',)}
	class Media:
	    js = TINY_MCE_TEXTAREAS
	
admin.site.register(StaticContent, StaticContentAdmin)
