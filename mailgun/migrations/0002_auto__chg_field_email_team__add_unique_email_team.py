# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Email.team'
        db.alter_column(u'mailgun_email', 'team_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['team.Team'], unique=True, null=True))
        # Adding unique constraint on 'Email', fields ['team']
        db.create_unique(u'mailgun_email', ['team_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Email', fields ['team']
        db.delete_unique(u'mailgun_email', ['team_id'])


        # Changing field 'Email.team'
        db.alter_column(u'mailgun_email', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Team'], null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mailgun.email': {
            'Meta': {'object_name': 'Email'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Job']", 'null': 'True', 'blank': 'True'}),
            'list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'team': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['team.Team']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'member.job': {
            'Meta': {'object_name': 'Job'},
            'bestuur': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'member.memberjob': {
            'Meta': {'object_name': 'MemberJob'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Job']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Person']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'member.person': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Person'},
            'account_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'citizenship': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'discount': ('django.db.models.fields.CharField', [], {'default': "'1NO'", 'max_length': '3'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'1M'", 'max_length': '2'}),
            'house_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'house_number_extension': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'iban': ('django_iban.fields.IBANField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'iban_authorisation': ('django.db.models.fields.CharField', [], {'default': "'1OK'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['member.Job']", 'through': u"orm['member.MemberJob']", 'symmetrical': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nfb_membership': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'other_club': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'playing_level': ('django.db.models.fields.CharField', [], {'default': "'1DN'", 'max_length': '3'}),
            'preposition': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'})
        },
        u'team.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'roster': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['member.Person']", 'through': u"orm['team.TeamMember']", 'symmetrical': 'False'})
        },
        u'team.teammember': {
            'Meta': {'ordering': "['status', 'member__last_name']", 'unique_together': "(['team', 'member'],)", 'object_name': 'TeamMember'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Person']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'2PL'", 'max_length': '3'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Team']"})
        }
    }

    complete_apps = ['mailgun']