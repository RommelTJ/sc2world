# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Player'
        db.create_table('player_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bnetnick', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, db_index=True)),
            ('charactercode', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
            ('zoom', self.gf('django.db.models.fields.IntegerField')()),
            ('details', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('player', ['Player'])


    def backwards(self, orm):
        
        # Deleting model 'Player'
        db.delete_table('player_player')


    models = {
        'player.player': {
            'Meta': {'object_name': 'Player'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'bnetnick': ('django.db.models.fields.CharField', [], {'unique': 'False', 'max_length': '100'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'charactercode': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'zoom': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['player']
