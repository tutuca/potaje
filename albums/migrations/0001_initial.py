# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table('albums_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('albums', ['Section'])

        # Adding model 'Album'
        db.create_table('albums_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['albums.Section'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('albums', ['Album'])

        # Adding model 'Picture'
        db.create_table('albums_picture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(blank=True, max_length=128, null=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['albums.Album'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('albums', ['Picture'])


    def backwards(self, orm):
        # Deleting model 'Section'
        db.delete_table('albums_section')

        # Deleting model 'Album'
        db.delete_table('albums_album')

        # Deleting model 'Picture'
        db.delete_table('albums_picture')


    models = {
        'albums.album': {
            'Meta': {'object_name': 'Album'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['albums.Section']"})
        },
        'albums.picture': {
            'Meta': {'object_name': 'Picture'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['albums.Album']"}),
            'caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'albums.section': {
            'Meta': {'object_name': 'Section', 'ordering': "('id',)"},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['albums']