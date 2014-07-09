# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Div'
        db.delete_table(u'team_div')

        # Deleting model 'Surface'
        db.delete_table(u'team_surface')

        # Deleting model 'TeamMemberStatus'
        db.delete_table(u'team_teammemberstatus')


        # Renaming column for 'TournamentTeam.div' to match new field type.
        db.rename_column(u'team_tournamentteam', 'div_id', 'div')
        # Changing field 'TournamentTeam.div'
        db.alter_column(u'team_tournamentteam', 'div', self.gf('django.db.models.fields.CharField')(max_length=2))
        # Removing index on 'TournamentTeam', fields ['div']
        db.delete_index(u'team_tournamentteam', ['div_id'])


        # Renaming column for 'TeamMember.status' to match new field type.
        db.rename_column(u'team_teammember', 'status_id', 'status')
        # Changing field 'TeamMember.status'
        db.alter_column(u'team_teammember', 'status', self.gf('django.db.models.fields.CharField')(max_length=2))
        # Removing index on 'TeamMember', fields ['status']
        db.delete_index(u'team_teammember', ['status_id'])


        # Renaming column for 'Tournament.surface' to match new field type.
        db.rename_column(u'team_tournament', 'surface_id', 'surface')
        # Changing field 'Tournament.surface'
        db.alter_column(u'team_tournament', 'surface', self.gf('django.db.models.fields.CharField')(max_length=2))
        # Removing index on 'Tournament', fields ['surface']
        db.delete_index(u'team_tournament', ['surface_id'])


    def backwards(self, orm):
        # Adding index on 'Tournament', fields ['surface']
        db.create_index(u'team_tournament', ['surface_id'])

        # Adding index on 'TeamMember', fields ['status']
        db.create_index(u'team_teammember', ['status_id'])

        # Adding index on 'TournamentTeam', fields ['div']
        db.create_index(u'team_tournamentteam', ['div_id'])

        # Adding model 'Div'
        db.create_table(u'team_div', (
            ('div', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'team', ['Div'])

        # Adding model 'Surface'
        db.create_table(u'team_surface', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('surface', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'team', ['Surface'])

        # Adding model 'TeamMemberStatus'
        db.create_table(u'team_teammemberstatus', (
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'team', ['TeamMemberStatus'])


        # Renaming column for 'TournamentTeam.div' to match new field type.
        db.rename_column(u'team_tournamentteam', 'div', 'div_id')
        # Changing field 'TournamentTeam.div'
        db.alter_column(u'team_tournamentteam', 'div_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Div']))

        # Renaming column for 'TeamMember.status' to match new field type.
        db.rename_column(u'team_teammember', 'status', 'status_id')
        # Changing field 'TeamMember.status'
        db.alter_column(u'team_teammember', 'status_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.TeamMemberStatus']))

        # Renaming column for 'Tournament.surface' to match new field type.
        db.rename_column(u'team_tournament', 'surface', 'surface_id')
        # Changing field 'Tournament.surface'
        db.alter_column(u'team_tournament', 'surface_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Surface']))

    models = {
        u'member.memberstatus': {
            'Meta': {'object_name': 'MemberStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'member.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'iban': ('django_iban.fields.IBANField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_thing': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.MemberStatus']"}),
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
            'Meta': {'object_name': 'TeamMember'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Person']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PL'", 'max_length': '2'}),
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
            'roster': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['member.Person']", 'symmetrical': 'False'}),
            'seed': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spirit_rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Team']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Tournament']"})
        }
    }

    complete_apps = ['team']