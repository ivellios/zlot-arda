# -*- coding: utf-8 -*-
from django.contrib import admin

from models import *

# dla wiadomości
class DokumentAdmin(admin.ModelAdmin):
	list_display = ('nazwa','plik')

class VoterAdmin(admin.ModelAdmin):
    list_display = ('email', 'hashset', 'vote', )
    list_filter = ['vote', ]

# rejestracja wraz z podaniem klasy konfigurującej PA
admin.site.register(Dokument, DokumentAdmin)
admin.site.register(Voter, VoterAdmin)

