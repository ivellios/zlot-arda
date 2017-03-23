# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Album(models.Model):
	name = models.CharField(max_length=255, verbose_name='Nazwa Albumu')
	slug = models.SlugField(max_length=255, unique=True, verbose_name='Odnośnik')
	mini =  models.ImageField(upload_to='ikonyGalerii', verbose_name='Ikona albumu')
	opis = models.TextField(verbose_name="Opis albumu")
	class Meta:
		verbose_name = "Album"
		verbose_name_plural = "Albumy"
	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name

class Obrazek(models.Model):
	album = models.ForeignKey(Album, verbose_name='Album')
	title = models.CharField(max_length=255, verbose_name='Opis',blank=True)
	image =  models.ImageField(upload_to='albums', verbose_name='Obrazek')
	class Meta:
		verbose_name = "Obrazek"
		verbose_name_plural = "Obrazki"
	def __str__(self):
		return self.title
	def __unicode__(self):
		return self.title
