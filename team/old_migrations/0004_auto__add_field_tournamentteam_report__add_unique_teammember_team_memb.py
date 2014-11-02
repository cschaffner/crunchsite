# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TournamentTeam.report'
        db.add_column(u'team_tournamentteam', 'report',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True),
                      keep_default=False)

        # Adding unique constraint on 'TeamMember', fields ['team', 'member']
        db.create_unique(u'team_teammember', ['team_id', 'member_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'TeamMember', fields ['team', 'member']
        db.delete_unique(u'team_teammember', ['team_id', 'member_id'])

        # Deleting field 'TournamentTeam.report'
        db.delete_column(u'team_tournamentteam', 'report_id')


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
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
        },
        u'team.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
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
        },
        u'team.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_teams': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'surface': ('django.db.models.fields.CharField', [], {'default': "'GR'", 'max_length': '2'}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['team.Team']", 'through': u"orm['team.TournamentTeam']", 'symmetrical': 'False'})
        },
        u'team.tournamentteam': {
            'Meta': {'object_name': 'TournamentTeam'},
            'div': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '2'}),
            'final_rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'roster': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['member.Person']", 'symmetrical': 'False'}),
            'seed': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spirit_rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Team']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Tournament']"})
        }
    }

    complete_apps = ['team']