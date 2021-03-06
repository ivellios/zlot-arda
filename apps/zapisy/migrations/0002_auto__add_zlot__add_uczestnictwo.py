# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Zlot'
        db.create_table('zapisy_zlot', (
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('rok', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('koniec', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('zapisy', ['Zlot'])

        # Adding M2M table for field plemiona on 'Zlot'
        db.create_table('zapisy_zlot_plemiona', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('zlot', models.ForeignKey(orm['zapisy.zlot'], null=False)),
            ('plemie', models.ForeignKey(orm['zapisy.plemie'], null=False))
        ))
        db.create_unique('zapisy_zlot_plemiona', ['zlot_id', 'plemie_id'])

        # Adding model 'Uczestnictwo'
        db.create_table('zapisy_uczestnictwo', (
            ('caly', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('od', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('do', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('zlot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Zlot'])),
            ('uczestnik', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Uczestnik'])),
            ('zaplacil', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('plemie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Plemie'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('zapisy', ['Uczestnictwo'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Zlot'
        db.delete_table('zapisy_zlot')

        # Removing M2M table for field plemiona on 'Zlot'
        db.delete_table('zapisy_zlot_plemiona')

        # Deleting model 'Uczestnictwo'
        db.delete_table('zapisy_uczestnictwo')
    
    
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
            'plemie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Plemie']"}),
            'urodzony': ('django.db.models.fields.DateField', [], {}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'zaplacil': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'zapisy.zlot': {
            'Meta': {'object_name': 'Zlot'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'koniec': ('django.db.models.fields.DateField', [], {}),
            'plemiona': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['zapisy.Plemie']", 'symmetrical': 'False'}),
            'rok': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
        }
    }
    
    complete_apps = ['zapisy']
