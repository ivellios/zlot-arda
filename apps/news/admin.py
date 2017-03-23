# -*- coding: utf-8 -*-
from django.contrib import admin

from news.models import *
from common import TINY_MCE_TEXTAREAS

# dla kategorii
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','icon')
	prepopulated_fields = {'slug': ('name',)}
	
# dla wiadomości
class NewsAdmin(admin.ModelAdmin):
	list_display = ('title','date','slug')
	prepopulated_fields = {'slug': ('title',)}
	class Media:
	    js = TINY_MCE_TEXTAREAS

# rejestracja wraz z podaniem klasy konfigurującej PA
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)

