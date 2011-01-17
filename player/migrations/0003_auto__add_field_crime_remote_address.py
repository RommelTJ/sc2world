# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Player.remote_address'
        db.add_column('player_player', 'remote_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Player.remote_address'
        db.delete_column('player_player', 'remote_address')


    models = {
        'player.player': {
            'Meta': {'object_name': 'Player'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'bnetnick': ('django.db.models.fields.CharField', [], {'unique': 'False', 'max_length': '100'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'charactercode': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'remote_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'zoom': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['player']
