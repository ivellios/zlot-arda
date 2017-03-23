# -*- coding:utf-8 -*-

from django.db import models

class Patron(models.Model):
    nazwa = models.CharField(u"Nazwa", max_length=255)
    opis = models.TextField(u"Opis", blank = True, null = True)
    url = models.URLField(u"URL")
    banner_small = models.ImageField(u"Mały banner/logo", help_text=u"wyświetlane w blokach, maksymalna szerokość 220px", upload_to="patroni")
    banner = models.ImageField(u"Duży banner", help_text=u"Banner na stronę patronów", upload_to="patroni_bannery")
    kolejnosc = models.IntegerField(u"Kolejność", default=100)
    
    def __unicode__(self):
        return self.nazwa
    
    class Meta:
        verbose_name=u"Patron"
        verbose_name_plural=u"Patroni"
        ordering = ['kolejnosc']

class Sponsor(models.Model):
    nazwa = models.CharField(u"Nazwa", max_length=255)
    url = models.URLField(u"URL")
    banner_small = models.ImageField(u"Mały banner/logo", help_text=u"wyświetlane w blokach, maksymalna szerokość 230px / full ", upload_to="sponsorzy")
    banner = models.ImageField(u"Duży banner", help_text=u"Banner na stronę patronów", upload_to="sponsorzy_bannery")
    kolejnosc = models.IntegerField(u"Kolejność", default=100)
    
    def __unicode__(self):
        return self.nazwa

    class Meta:
        verbose_name = u"Sponsor"
        verbose_name_plural = u"Sponsorzy"
        ordering = ['kolejnosc']