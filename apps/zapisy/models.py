# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, UserManager

# Create your models here.

class Plemie(models.Model):
    nazwa = models.CharField("Nazwa plemienia",max_length=255)
    showonpage = models.BooleanField('Pokaż na stronie',default=False)
    can_register = models.BooleanField(u"Można się zapisać", default=True)
    rekruter_mail = models.CharField("Email rekrutującej osoby",max_length=255)
    nick = models.CharField("Nick rekrutera",max_length=255)
    gg = models.CharField("GG rekrutera",max_length=255,blank=True)
    opis = models.TextField('Opis plemienia',blank=True)

    class Meta:
        verbose_name = u"Plemię"
        verbose_name_plural = 'Plemiona'
        ordering = ['nazwa']

    def __unicode__(self):
        return self.nazwa

class Zlot(models.Model):
    rok = models.IntegerField("Rok zlotu",unique=True)
    start = models.DateField("Początek Zlotu")
    koniec = models.DateField("Koniec Zlotu")
    zapisy_otwarte = models.BooleanField(u"Czy zapisy są otwarte",default=False)
    miejsce = models.CharField(u"Miejsce zlotu",max_length=255,blank=True,null=True)

    class Meta:
        verbose_name="Zlot"
        verbose_name_plural="Zloty"

    def __unicode__(self):
        return "Zlot Arda "+str(self.rok)

class Larp(models.Model):
    zlot = models.ForeignKey(Zlot)
    nazwa = models.CharField(u"Nazwa", max_length = 255)
    slug = models.SlugField(u'Slug')
    opis = models.TextField(u"Opis")
    zapisy_otwarte = models.BooleanField(u"Czy zapisy są otwarte", default = False)
    obraz = models.ImageField(u"Obraz pod fb", upload_to = 'larpy', blank = True)

    class Meta:
        verbose_name = u"Larp"
        verbose_name_plural = u"Larpy"

    def __unicode__(self):
        return self.nazwa

class Frakcja(models.Model):
    larp = models.ForeignKey(Larp)
    nazwa = models.CharField(u"Nazwa", max_length = 255)
    slug = models.SlugField(u"Slug")
    opis = models.TextField(u"Opis")
    wprowadzenie = models.TextField(u"Wprowadzenie", blank = True, null = True)
    zasady_rekrutacji = models.TextField(u"Zasady przyjmowania", blank = True, null = True)
    mozna_wybrac = models.BooleanField(u'Czy można wybrać w zapisie?', default = True)
    dostepny_opis = models.BooleanField(u"Czy można zobaczyć opis?", default = True)
    dostepna_rekrutacja = models.BooleanField(u"Czy można zobaczyć reguły rekrutacji?", default = True)
    limit = models.IntegerField(u'Limit miejsc', help_text=u"Limit miejsc we frakcji bez zarezerwowanych miejsc", blank = True, null = True)
    minimum = models.IntegerField(u'Minimum osób', help_text=u"Minimalna ilość osób, aby frakcja mogła w ogóle zaistnieć w grze", blank = True, null = True)
    rezerwowane = models.IntegerField(u"Zarezerwowane miejsca", help_text=u"Miejsca zarezerwowane dla zgłoszonych postaci", blank = True, null = True)
    image = models.ImageField("Obraz", upload_to='frakcje', blank=True)

    class Meta:
        verbose_name = u'Frakcja'
        verbose_name_plural = u'Frakcje'
        ordering = ['nazwa']

    def __unicode__(self):
        return self.nazwa

    def wolne_miejsca(self):
        if self.limit:
            return self.limit-self.frakcjauczestnik_set.filter(rezerwowany=False).count()
        return 0;

    def zajete_miejsca(self):
        if self.frakcjauczestnik_set:
            return self.frakcjauczestnik_set.count()
        return 0


class Uczestnik(User):
    email_sent = models.BooleanField("Wyslane powiadomienie", default = False) # powiadomienie o zmianie hasła

    objects = UserManager()

    def get_register_hash(self):
        import hashlib
        return hashlib.sha1('magicznykluczgandalfa' + self.username.encode('utf-8') + self.email).hexdigest()

    class Meta:
        verbose_name = 'Uczestnik'
        verbose_name_plural = 'Uczestnicy'
        ordering = ['username']

    def __unicode__(self):
           return u"%s" % self.username


class Uczestnictwo(models.Model):
    zlot = models.ForeignKey(Zlot)
    uczestnik = models.ForeignKey(Uczestnik)
    zaplacil = models.BooleanField(u"Zapłacił za zlot",default=False)
    caly = models.BooleanField(u"Czy na cały zlot",default=True)
    od = models.DateField("Od",help_text=u"Jeżeli jedziesz na część zlotu, podaj od kiedy będziesz (RRRR-MM-DD)<br/>W przeciwnym razie pozostaw puste.",blank=True,null=True)
    do = models.DateField("Do",help_text=u"Jeżeli jedziesz na część zlotu, podaj do kiedy będziesz (RRRR-MM-DD)<br/>W przeciwnym razie pozostaw puste.",blank=True,null=True)
    timestamp = models.DateTimeField("Dodano", auto_now_add=True, default="2012-05-01")

    class Meta:
        verbose_name="Uczestnictwo"
        verbose_name_plural="Uczestnictwa"

    def __unicode__(self):
        return unicode(self.uczestnik)+" @ "+unicode(self.zlot)

    def email(self):
        return self.uczestnik.email

class FrakcjaUczestnik(models.Model):
    frakcja = models.ForeignKey(Frakcja)
    uczestnik = models.ForeignKey(Uczestnik)
    timestamp = models.DateTimeField("Dodano", auto_now_add=True)
    rezerwowany = models.BooleanField(u"Rezerwowany", default=False)

    class Meta:
        verbose_name = u"Zapis do Frakcji"
        verbose_name_plural = u"Zapisy do Frakcji"

    def __unicode__(self):
        return unicode(self.uczestnik)+" @ "+unicode(self.frakcja)

class Wpis(models.Model):
    """ Pojedynczy wpis w dyskusji pomiędzy członkami danej frakcji """
    fu = models.ForeignKey(FrakcjaUczestnik) # musi być uczestnikiem frakcji
    text = models.TextField(u"Wiadomość")
    timestamp = models.DateTimeField(u"Dodano", auto_now_add = True)

    class Meta:
        verbose_name = u"Wpis w dyskusji frakcji"
        verbose_name_plural = u"Wpisy w dyskusji frakcji"
        ordering = ['timestamp']
