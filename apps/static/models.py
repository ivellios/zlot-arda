# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class StaticContent(models.Model):
	title = models.CharField(max_length=255,verbose_name='Nazwa strony')
	slug = models.SlugField(max_length=25,unique=True,verbose_name="Odnośnik")
	content = models.TextField(verbose_name='Treść statyczna')
	image = models.ImageField("Obraz", upload_to='statics', blank=True)
	class Meta:
		verbose_name = "Strona statyczna"
		verbose_name_plural = "Strony statyczne"
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return '/static/'+ self.slug + '/'
