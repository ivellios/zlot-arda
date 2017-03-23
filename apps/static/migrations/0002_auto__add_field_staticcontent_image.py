# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'StaticContent.image'
        db.add_column('static_staticcontent', 'image', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'StaticContent.image'
        db.delete_column('static_staticcontent', 'image')
    
    
    models = {
        'static.staticcontent': {
            'Meta': {'object_name': 'StaticContent'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '25', 'unique': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['static']
