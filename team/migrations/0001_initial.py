# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TeamMemberStatus'
        db.create_table(u'team_teammemberstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'team', ['TeamMemberStatus'])

        # Adding model 'Team'
        db.create_table(u'team_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'team', ['Team'])

        # Adding model 'TeamMember'
        db.create_table(u'team_teammember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Team'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Person'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.TeamMemberStatus'])),
        ))
        db.send_create_signal(u'team', ['TeamMember'])

        # Adding model 'Surface'
        db.create_table(u'team_surface', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('surface', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'team', ['Surface'])

        # Adding model 'Div'
        db.create_table(u'team_div', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('div', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'team', ['Div'])

        # Adding model 'Tournament'
        db.create_table(u'team_tournament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('number_teams', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('surface', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Surface'])),
        ))
        db.send_create_signal(u'team', ['Tournament'])

        # Adding model 'TournamentTeam'
        db.create_table(u'team_tournamentteam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Team'])),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Tournament'])),
            ('div', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Div'])),
            ('seed', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('final_rank', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('spirit_rank', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'team', ['TournamentTeam'])

        # Adding M2M table for field roster on 'TournamentTeam'
        m2m_table_name = db.shorten_name(u'team_tournamentteam_roster')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tournamentteam', models.ForeignKey(orm[u'team.tournamentteam'], null=False)),
            ('person', models.ForeignKey(orm[u'member.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tournamentteam_id', 'person_id'])


    def backwards(self, orm):
        # Deleting model 'TeamMemberStatus'
        db.delete_table(u'team_teammemberstatus')

        # Deleting model 'Team'
        db.delete_table(u'team_team')

        # Deleting model 'TeamMember'
        db.delete_table(u'team_teammember')

        # Deleting model 'Surface'
        db.delete_table(u'team_surface')

        # Deleting model 'Div'
        db.delete_table(u'team_div')

        # Deleting model 'Tournament'
        db.delete_table(u'team_tournament')

        # Deleting model 'TournamentTeam'
        db.delete_table(u'team_tournamentteam')

        # Removing M2M table for field roster on 'TournamentTeam'
        db.delete_table(db.shorten_name(u'team_tournamentteam_roster'))


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
        u'team.div': {
            'Meta': {'object_name': 'Div'},
            'div': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'team.surface': {
            'Meta': {'object_name': 'Surface'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'surface': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.TeamMemberStatus']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Team']"})
        },
        u'team.teammemberstatus': {
            'Meta': {'object_name': 'TeamMemberStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'surface': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Surface']"}),
            'team': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['team.Team']", 'through': u"orm['team.TournamentTeam']", 'symmetrical': 'False'})
        },
        u'team.tournamentteam': {
            'Meta': {'object_name': 'TournamentTeam'},
            'div': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Div']"}),
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