# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Patron.opis'
        db.add_column(u'patroni_patron', 'opis',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Patron.opis'
        db.delete_column(u'patroni_patron', 'opis')


    models = {
        u'patroni.patron': {
            'Meta': {'ordering': "['kolejnosc']", 'object_name': 'Patron'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'banner_small': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kolejnosc': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opis': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'patroni.sponsor': {
            'Meta': {'ordering': "['kolejnosc']", 'object_name': 'Sponsor'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'banner_small': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kolejnosc': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['patroni']