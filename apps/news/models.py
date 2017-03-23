# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name='Nazwa Kategorii')
	slug = models.SlugField(max_length=255, unique=True, verbose_name='Odnośnik')
	icon =  models.ImageField(upload_to='icons', verbose_name='Ikonka Kategorii', blank=True)
	class Meta:
		verbose_name = "Kategoria"
		verbose_name_plural = "Kategorie"
	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name

import datetime
		
class News(models.Model):
	category = models.ManyToManyField(Category, verbose_name='Kategorie')
	title = models.CharField(max_length=255, verbose_name=u'Tytuł')
	slug = models.SlugField(max_length=255, unique=True, verbose_name='Odnośnik')
	text = models.TextField(verbose_name=u'Treść')
	image = models.ImageField("Ilustracja", upload_to='news', help_text="max_width=530px", blank=True, null=True)
	date = models.DateTimeField(verbose_name='Data dodania',auto_now_add=True)

	class Meta:
		verbose_name = "Wiadomość"
		verbose_name_plural = "Wiadomości"
		ordering = ['-date']
	def __str__(self):
		return self.title
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return '/news/' + self.slug + '/'
