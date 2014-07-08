from django.db import models
from member.models import Person
from django_countries.fields import CountryField


class TeamMemberStatus(models.Model):
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return self.status



class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    roster = models.ManyToManyField(Person, through='TeamMember')

    def __unicode__(self):
        return self.name



class TeamMember(models.Model):
    team = models.ForeignKey(Team)
    member = models.ForeignKey(Person)
    status = models.ForeignKey(TeamMemberStatus)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.status, self.team, self.member)


class Surface(models.Model):
    surface = models.CharField(max_length=100)

    def __unicode__(self):
        return self.surface


class Div(models.Model):
    div = models.CharField(max_length=100, verbose_name='Division')

    def __unicode__(self):
        return self.div




class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    number_teams = models.PositiveSmallIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField()
    link = models.URLField(null=True, blank=True)
    surface = models.ForeignKey(Surface)

    team = models.ManyToManyField(Team, through='TournamentTeam')

    def __unicode__(self):
        return self.name




class TournamentTeam(models.Model):
    team = models.ForeignKey(Team)
    tournament = models.ForeignKey(Tournament)
    div = models.ForeignKey(Div)

    seed = models.PositiveSmallIntegerField(null=True, blank=True)
    final_rank = models.PositiveSmallIntegerField(null=True, blank=True)
    spirit_rank = models.PositiveSmallIntegerField(null=True, blank=True)
    roster = models.ManyToManyField(Person)

    def __unicode__(self):
        return u'{0} {1}'.format(self.team, self.tournament)

