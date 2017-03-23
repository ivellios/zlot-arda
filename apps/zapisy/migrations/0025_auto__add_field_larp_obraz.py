# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Larp.obraz'
        db.add_column('zapisy_larp', 'obraz', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Larp.obraz'
        db.delete_column('zapisy_larp', 'obraz')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'zapisy.frakcja': {
            'Meta': {'object_name': 'Frakcja'},
            'dostepna_rekrutacja': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'dostepny_opis': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'larp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Larp']"}),
            'limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minimum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mozna_wybrac': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'rezerwowane': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'wprowadzenie': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zasady_rekrutacji': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'zapisy.frakcjauczestnik': {
            'Meta': {'object_name': 'FrakcjaUczestnik'},
            'frakcja': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Frakcja']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rezerwowany': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'uczestnik': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Uczestnik']"})
        },
        'zapisy.larp': {
            'Meta': {'object_name': 'Larp'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obraz': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'zapisy_otwarte': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'zlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Zlot']"})
        },
        'zapisy.plemie': {
            'Meta': {'object_name': 'Plemie'},
            'can_register': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
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
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': "'2012-05-01'", 'auto_now_add': 'True', 'blank': 'True'}),
            'uczestnik': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Uczestnik']"}),
            'zaplacil': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'zlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Zlot']"})
        },
        'zapisy.uczestnik': {
            'Meta': {'object_name': 'Uczestnik', '_ormbases': ['auth.User']},
            'email_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'zapisy.wpis': {
            'Meta': {'object_name': 'Wpis'},
            'fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.FrakcjaUczestnik']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'zapisy.zlot': {
            'Meta': {'object_name': 'Zlot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'koniec': ('django.db.models.fields.DateField', [], {}),
            'miejsce': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rok': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'zapisy_otwarte': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        }
    }
    
    complete_apps = ['zapisy']
