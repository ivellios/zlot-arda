# -*- coding: utf-8 -*-
from django.contrib import admin

from galeria.models import *

class ChoiceInline(admin.TabularInline):
    model = Obrazek
    extra = 5

# dla kategorii
class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name',)
	prepopulated_fields = {'slug': ('name',)}
	inlines = [ChoiceInline]
	
	
# dla wiadomości
class ObrazekAdmin(admin.ModelAdmin):
	list_display = ('title',)

# rejestracja wraz z podaniem klasy konfigurującej PA
admin.site.register(Album, AlbumAdmin)
#admin.site.register(Obrazek, ObrazekAdmin)

