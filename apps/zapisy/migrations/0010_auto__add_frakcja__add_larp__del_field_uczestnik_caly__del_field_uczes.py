# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Frakcja'
        db.create_table('zapisy_frakcja', (
            ('wprowadzenie', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('larp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Larp'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('opis', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('zapisy', ['Frakcja'])

        # Adding model 'Larp'
        db.create_table('zapisy_larp', (
            ('zapisy_otwarte', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('zlot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Zlot'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('opis', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('zapisy', ['Larp'])

        # Deleting field 'Uczestnik.caly'
        db.delete_column('zapisy_uczestnik', 'caly')

        # Deleting field 'Uczestnik.do'
        db.delete_column('zapisy_uczestnik', 'do')

        # Deleting field 'Uczestnik.od'
        db.delete_column('zapisy_uczestnik', 'od')

        # Deleting field 'Uczestnik.email_sent'
        db.delete_column('zapisy_uczestnik', 'email_sent')

        # Deleting field 'Uczestnik.urodzony'
        db.delete_column('zapisy_uczestnik', 'urodzony')

        # Deleting field 'Uczestnik.zaplacil'
        db.delete_column('zapisy_uczestnik', 'zaplacil')

        # Deleting field 'Uczestnik.plemie'
        db.delete_column('zapisy_uczestnik', 'plemie_id')

        # Removing M2M table for field plemiona on 'Zlot'
        db.delete_table('zapisy_zlot_plemiona')

        # Changing field 'Uczestnictwo.plemie'
        db.alter_column('zapisy_uczestnictwo', 'plemie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Plemie'], blank=True))
    
    
    def backwards(self, orm):
        
        # Deleting model 'Frakcja'
        db.delete_table('zapisy_frakcja')

        # Deleting model 'Larp'
        db.delete_table('zapisy_larp')

        # Adding field 'Uczestnik.caly'
        db.add_column('zapisy_uczestnik', 'caly', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)

        # Adding field 'Uczestnik.do'
        db.add_column('zapisy_uczestnik', 'do', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Uczestnik.od'
        db.add_column('zapisy_uczestnik', 'od', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Uczestnik.email_sent'
        db.add_column('zapisy_uczestnik', 'email_sent', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'Uczestnik.urodzony'
        db.add_column('zapisy_uczestnik', 'urodzony', self.gf('django.db.models.fields.DateField')(default=1988), keep_default=False)

        # Adding field 'Uczestnik.zaplacil'
        db.add_column('zapisy_uczestnik', 'zaplacil', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'Uczestnik.plemie'
        db.add_column('zapisy_uczestnik', 'plemie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Plemie'], null=True, blank=True), keep_default=False)

        # Adding M2M table for field plemiona on 'Zlot'
        db.create_table('zapisy_zlot_plemiona', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('zlot', models.ForeignKey(orm['zapisy.zlot'], null=False)),
            ('plemie', models.ForeignKey(orm['zapisy.plemie'], null=False))
        ))
        db.create_unique('zapisy_zlot_plemiona', ['zlot_id', 'plemie_id'])

        # Changing field 'Uczestnictwo.plemie'
        db.alter_column('zapisy_uczestnictwo', 'plemie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zapisy.Plemie']))
    
    
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'larp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Larp']"}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'wprowadzenie': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'zapisy.larp': {
            'Meta': {'object_name': 'Larp'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
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
            'plemie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Plemie']", 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': "'2012-05-01'", 'auto_now_add': 'True', 'blank': 'True'}),
            'uczestnik': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Uczestnik']"}),
            'zaplacil': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'zlot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['zapisy.Zlot']"})
        },
        'zapisy.uczestnik': {
            'Meta': {'object_name': 'Uczestnik', '_ormbases': ['auth.User']},
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
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
