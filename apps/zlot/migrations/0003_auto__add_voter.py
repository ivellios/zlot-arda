# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Voter'
        db.create_table(u'zlot_voter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hashset', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vote', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'zlot', ['Voter'])


    def backwards(self, orm):
        # Deleting model 'Voter'
        db.delete_table(u'zlot_voter')


    models = {
        u'zlot.dokument': {
            'Meta': {'object_name': 'Dokument'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mozna_pobrac': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'plik': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'zlot.voter': {
            'Meta': {'object_name': 'Voter'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'hashset': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['zlot']