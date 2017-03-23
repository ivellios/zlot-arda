# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Dokument.mozna_pobrac'
        db.add_column('zlot_dokument', 'mozna_pobrac', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Dokument.mozna_pobrac'
        db.delete_column('zlot_dokument', 'mozna_pobrac')
    
    
    models = {
        'zlot.dokument': {
            'Meta': {'object_name': 'Dokument'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mozna_pobrac': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'plik': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['zlot']
