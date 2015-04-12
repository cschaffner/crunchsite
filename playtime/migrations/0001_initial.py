# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Field'
        db.create_table(u'playtime_field', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playtime.FieldLocation'])),
        ))
        db.send_create_signal(u'playtime', ['Field'])

        # Adding model 'FieldLocation'
        db.create_table(u'playtime_fieldlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'playtime', ['FieldLocation'])

        # Adding model 'FieldSlot'
        db.create_table(u'playtime_fieldslot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'playtime', ['FieldSlot'])

        # Adding model 'FieldEvent'
        db.create_table(u'playtime_fieldevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('fields', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playtime.Field'])),
            ('field_slot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playtime.FieldSlot'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'playtime', ['FieldEvent'])


    def backwards(self, orm):
        # Deleting model 'Field'
        db.delete_table(u'playtime_field')

        # Deleting model 'FieldLocation'
        db.delete_table(u'playtime_fieldlocation')

        # Deleting model 'FieldSlot'
        db.delete_table(u'playtime_fieldslot')

        # Deleting model 'FieldEvent'
        db.delete_table(u'playtime_fieldevent')


    models = {
        u'playtime.field': {
            'Meta': {'object_name': 'Field'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['playtime.FieldLocation']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'playtime.fieldevent': {
            'Meta': {'object_name': 'FieldEvent'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'field_slot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['playtime.FieldSlot']"}),
            'fields': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['playtime.Field']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'playtime.fieldlocation': {
            'Meta': {'object_name': 'FieldLocation'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'playtime.fieldslot': {
            'Meta': {'object_name': 'FieldSlot'},
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['playtime']