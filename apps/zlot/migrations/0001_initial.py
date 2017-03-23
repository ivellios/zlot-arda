# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Dokument'
        db.create_table('zlot_dokument', (
            ('plik', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('opis', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('zlot', ['Dokument'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Dokument'
        db.delete_table('zlot_dokument')
    
    
    models = {
        'zlot.dokument': {
            'Meta': {'object_name': 'Dokument'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'plik': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['zlot']
