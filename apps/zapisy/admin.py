# -*- coding: utf-8 -*-
from models import *

from django.contrib import admin
from common import TINY_MCE_TEXTAREAS
from django.contrib.auth.admin import UserAdmin

class LarpAdmin(admin.ModelAdmin):
    list_filter = ['zlot', ]
    class Media:
        js = TINY_MCE_TEXTAREAS

class FrakcjaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'larp', 'mozna_wybrac', 'zapelnienie', 'minimum', 'rezerwowane', 'dostepny_opis', 'dostepna_rekrutacja']
    list_filter = ['larp', 'mozna_wybrac']

    def get_wolne_miejsca(self, obj):
        return '%s/%s'%(obj.wolne_miejsca(), obj.limit)
    get_wolne_miejsca.short_description = 'Wolne miejsca'

    def zapelnienie(self, obj):
        if obj.limit and obj.rezerwowane:
            return '%s/%s'%(obj.zajete_miejsca(), obj.limit+obj.rezerwowane)
        return u"Nie określono"
    zapelnienie.short_description = 'Zajęte miejsca'

    class Media:
        js = TINY_MCE_TEXTAREAS

class PlemieAdmin(admin.ModelAdmin):
    list_display = ['nazwa','rekruter_mail','nick','gg', 'can_register', 'showonpage']
    class Media:
        js = TINY_MCE_TEXTAREAS

class UczestnikAdmin(admin.ModelAdmin):
    list_display = ('username','email','date_joined','email_sent',)
    list_filter = ['is_staff','is_active','is_superuser']

class ZlotAdmin(admin.ModelAdmin):
    list_display = ('rok','start','koniec','zapisy_otwarte','miejsce',)
    list_filter = ['rok',]
admin.site.register(Zlot, ZlotAdmin)

def set_zaplacil(modeladmin, request, queryset):
    queryset.update(zaplacil = True)
set_zaplacil.short_description = u"Oznacz jako zapłacone"

class UczestnictwoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','caly','od','do','zaplacil','zlot','uczestnik', 'email', 'timestamp', )
    list_filter = ['zaplacil','caly','zlot']
    search_fields = ['uczestnik__username', 'zlot__rok', ]
    actions = [set_zaplacil,]


class FrakcjaUczestnikAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'timestamp', 'frakcja', 'rezerwowany']
    list_filter = ['frakcja', ]
    search_fields = ['frakcja__larp__nazwa', 'uczestnik__username']

class WpisAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'fu']

admin.site.register(Uczestnictwo, UczestnictwoAdmin)

admin.site.register(Uczestnik, UczestnikAdmin)
admin.site.register(Plemie, PlemieAdmin)
admin.site.register(Frakcja, FrakcjaAdmin)
admin.site.register(Larp, LarpAdmin)
admin.site.register(FrakcjaUczestnik, FrakcjaUczestnikAdmin)
admin.site.register(Wpis, WpisAdmin)
