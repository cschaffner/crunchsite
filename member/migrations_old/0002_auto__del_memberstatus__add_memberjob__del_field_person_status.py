# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'MemberStatus'
        db.delete_table(u'member_memberstatus')

        # Adding model 'MemberJob'
        db.create_table(u'member_memberjob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.CharField')(default='1PL', max_length=3)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='jobs', to=orm['member.Person'])),
        ))
        db.send_create_signal(u'member', ['MemberJob'])

        # Deleting field 'Person.status'
        db.delete_column(u'member_person', 'status_id')


    def backwards(self, orm):
        # Adding model 'MemberStatus'
        db.create_table(u'member_memberstatus', (
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'member', ['MemberStatus'])

        # Deleting model 'MemberJob'
        db.delete_table(u'member_memberjob')

        # Adding field 'Person.status'
        db.add_column(u'member_person', 'status',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=u'', to=orm['member.MemberStatus']),
                      keep_default=False)


    models = {
        u'member.memberjob': {
            'Meta': {'object_name': 'MemberJob'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'default': "'1PL'", 'max_length': '3'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'jobs'", 'to': u"orm['member.Person']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'member.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'iban': ('django_iban.fields.IBANField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_thing': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'swift_bic': ('django_iban.fields.SWIFTBICField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['member']