# -*- coding: utf-8 -*-
from django.db import models

import os

# Create your models here.

class Dokument(models.Model):
  nazwa = models.CharField(max_length=255)
  plik = models.FileField('Plik',upload_to='files')
  opis = models.TextField()
  mozna_pobrac = models.BooleanField(u"Można pobrać", default = True)
  
  def __unicode__(self):
    return self.nazwa
  
  class Meta:
    verbose_name_plural = 'Dokumenty'

  def extension(self):
    name, extension = os.path.splitext(self.plik.name)
    return extension[-3:]

VOTINGS = (
		('R', 'Ravenne i Ataron'),
		('I', 'Isilya i Lejba'),
	)

import hashlib

class Voter(models.Model):
	email = models.CharField("Email", max_length = 255)
	hashset = models.CharField("Hash", max_length = 255)
	vote = models.CharField('Vote', max_length = 2, choices = VOTINGS, blank = True, null = True)

	def get_hash(self):
		return hashlib.sha224('voting'+self.email).hexdigest()
