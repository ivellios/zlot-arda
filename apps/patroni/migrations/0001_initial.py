# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Patron'
        db.create_table('patroni_patron', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('kolejnosc', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('banner_small', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('banner', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('patroni', ['Patron'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Patron'
        db.delete_table('patroni_patron')
    
    
    models = {
        'patroni.patron': {
            'Meta': {'object_name': 'Patron'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'banner_small': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kolejnosc': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['patroni']
