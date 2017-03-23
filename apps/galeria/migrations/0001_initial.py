# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Album'
        db.create_table('galeria_album', (
            ('mini', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True, db_index=True)),
            ('opis', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('galeria', ['Album'])

        # Adding model 'Obrazek'
        db.create_table('galeria_obrazek', (
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['galeria.Album'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('galeria', ['Obrazek'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Album'
        db.delete_table('galeria_album')

        # Deleting model 'Obrazek'
        db.delete_table('galeria_obrazek')
    
    
    models = {
        'galeria.album': {
            'Meta': {'object_name': 'Album'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mini': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'db_index': 'True'})
        },
        'galeria.obrazek': {
            'Meta': {'object_name': 'Obrazek'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['galeria.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }
    
    complete_apps = ['galeria']
