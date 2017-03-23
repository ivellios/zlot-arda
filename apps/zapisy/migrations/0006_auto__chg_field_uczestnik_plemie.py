# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Uczestnik.plemie'
        db.alter_column('zapisy_uczestnik', 'plemie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Plemie'], null=True, blank=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'Uczestnik.plemie'
        db.alter_column('zapisy_uczestnik', 'plemie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Plemie'], blank=True))
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'zapisy.plemie': {
            'Meta': {'object_name': 'Plemie'},
            'gg': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rekruter_mail': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'showonpage': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'zapisy.uczestnictwo': {
            'Meta': {'object_name': 'Uczestnictwo'},
            'caly': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'do': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'od': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'plemie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Plemie']"}),
            'uczestnik': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Uczestnik']"}),
            'zaplacil': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'zlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Zlot']"})
        },
        'zapisy.uczestnik': {
            'Meta': {'object_name': 'Uczestnik', '_ormbases': ['auth.User']},
            'caly': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'do': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'od': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'plemie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Plemie']", 'null': 'True', 'blank': 'True'}),
            'urodzony': ('django.db.models.fields.DateField', [], {}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'zaplacil': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'zapisy.zlot': {
            'Meta': {'object_name': 'Zlot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'koniec': ('django.db.models.fields.DateField', [], {}),
            'miejsce': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plemiona': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['zapisy.Plemie']", 'symmetrical': 'False'}),
            'rok': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'zapisy_otwarte': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        }
    }
    
    complete_apps = ['zapisy']
