# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TournamentTeamMember'
        db.create_table(u'team_tournamentteammember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournamentteam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.TournamentTeam'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Person'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='2PL', max_length=3)),
        ))
        db.send_create_signal(u'team', ['TournamentTeamMember'])

        # Adding unique constraint on 'TournamentTeamMember', fields ['tournamentteam', 'member']
        db.create_unique(u'team_tournamentteammember', ['tournamentteam_id', 'member_id'])

        # Adding model 'Competition'
        db.create_table(u'team_competition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('div', self.gf('django.db.models.fields.CharField')(default='1O', max_length=2)),
            ('number_divisions', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('number_teams', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('day1', self.gf('django.db.models.fields.DateField')()),
            ('day2', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('day3', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('day4', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('day1_lv_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('day2_lv_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('day3_lv_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('day4_lv_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'team', ['Competition'])

        # Adding model 'CompetitionTeam'
        db.create_table(u'team_competitionteam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Team'])),
            ('competition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.Competition'])),
            ('seed', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('final_rank', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('spirit_rank', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('report_day1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='report_day1', null=True, to=orm['cms.Placeholder'])),
            ('report_day2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='report_day2', null=True, to=orm['cms.Placeholder'])),
            ('report_day3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='report_day3', null=True, to=orm['cms.Placeholder'])),
            ('report_day4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='report_day4', null=True, to=orm['cms.Placeholder'])),
        ))
        db.send_create_signal(u'team', ['CompetitionTeam'])

        # Adding model 'CompetitionTeamMember'
        db.create_table(u'team_competitionteammember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('competitionteam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['team.CompetitionTeam'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member.Person'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='2PL', max_length=3)),
        ))
        db.send_create_signal(u'team', ['CompetitionTeamMember'])

        # Adding unique constraint on 'CompetitionTeamMember', fields ['competitionteam', 'member']
        db.create_unique(u'team_competitionteammember', ['competitionteam_id', 'member_id'])

        # Removing M2M table for field roster on 'TournamentTeam'
        db.delete_table(db.shorten_name(u'team_tournamentteam_roster'))


    def backwards(self, orm):
        # Removing unique constraint on 'CompetitionTeamMember', fields ['competitionteam', 'member']
        db.delete_unique(u'team_competitionteammember', ['competitionteam_id', 'member_id'])

        # Removing unique constraint on 'TournamentTeamMember', fields ['tournamentteam', 'member']
        db.delete_unique(u'team_tournamentteammember', ['tournamentteam_id', 'member_id'])

        # Deleting model 'TournamentTeamMember'
        db.delete_table(u'team_tournamentteammember')

        # Deleting model 'Competition'
        db.delete_table(u'team_competition')

        # Deleting model 'CompetitionTeam'
        db.delete_table(u'team_competitionteam')

        # Deleting model 'CompetitionTeamMember'
        db.delete_table(u'team_competitionteammember')

        # Adding M2M table for field roster on 'TournamentTeam'
        m2m_table_name = db.shorten_name(u'team_tournamentteam_roster')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tournamentteam', models.ForeignKey(orm[u'team.tournamentteam'], null=False)),
            ('person', models.ForeignKey(orm[u'member.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tournamentteam_id', 'person_id'])


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
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'member.person': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Person'},
            'description': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'iban': ('django_iban.fields.IBANField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_thing': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'swift_bic': ('django_iban.fields.SWIFTBICField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'team.competition': {
            'Meta': {'ordering': "['day1']", 'object_name': 'Competition'},
            'day1': ('django.db.models.fields.DateField', [], {}),
            'day1_lv_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'day2': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'day2_lv_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'day3': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'day3_lv_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'day4': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'day4_lv_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'div': ('django.db.models.fields.CharField', [], {'default': "'1O'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_divisions': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_teams': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'team.competitionteam': {
            'Meta': {'object_name': 'CompetitionTeam'},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Competition']"}),
            'final_rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report_day1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'report_day1'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'report_day2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'report_day2'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'report_day3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'report_day3'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'report_day4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'report_day4'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'roster': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['member.Person']", 'through': u"orm['team.CompetitionTeamMember']", 'symmetrical': 'False'}),
            'seed': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spirit_rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Team']"})
        },
        u'team.competitionteammember': {
            'Meta': {'ordering': "['status', 'member__last_name']", 'unique_together': "(['competitionteam', 'member'],)", 'object_name': 'CompetitionTeamMember'},
            'competitionteam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.CompetitionTeam']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Person']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'2PL'", 'max_length': '3'})
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
        },
        u'team.tournament': {
            'Meta': {'ordering': "['start_date']", 'object_name': 'Tournament'},
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
            'div': ('django.db.models.fields.CharField', [], {'default': "'1O'", 'max_length': '2'}),
            'final_rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'roster': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['member.Person']", 'through': u"orm['team.TournamentTeamMember']", 'symmetrical': 'False'}),
            'seed': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spirit_rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Team']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.Tournament']"})
        },
        u'team.tournamentteammember': {
            'Meta': {'ordering': "['status', 'member__last_name']", 'unique_together': "(['tournamentteam', 'member'],)", 'object_name': 'TournamentTeamMember'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member.Person']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'2PL'", 'max_length': '3'}),
            'tournamentteam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['team.TournamentTeam']"})
        }
    }

    complete_apps = ['team']