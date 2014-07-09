from django.db import models
from django.core.urlresolvers import reverse

from member.models import Person
from django_countries.fields import CountryField



class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    roster = models.ManyToManyField(Person, through='TeamMember')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team:detail', args=[self.pk])


class TeamMember(models.Model):
    CAPTAIN = '1CA'
    PLAYER = '2PL'
    TRAINER = '3TR'
    ALUMNI = '4AL'
    STATUS_CHOICES = (
        (CAPTAIN, 'captain'),
        (PLAYER, 'player'),
        (TRAINER, 'trainer'),
        (ALUMNI, 'alumni'),
    )
    STATUS_NAMES = dict((k,v) for k,v in STATUS_CHOICES)

    team = models.ForeignKey(Team)
    member = models.ForeignKey(Person)
    status = models.CharField(max_length=3,
                              choices=STATUS_CHOICES,
                              default=PLAYER)

    def __unicode__(self):
        return u'{1} ({0} of {2})'.format(self.STATUS_NAMES[self.status], self.member, self.team)

    def get_status(self):
        return self.STATUS_NAMES[self.status]

    class Meta:
        ordering = ['status', 'member__last_name']


class Tournament(models.Model):
    GRASS = 'GR'
    BEACH = 'BE'
    INDOOR = 'IN'
    SURFACE_CHOICES = (
        (GRASS, 'grass'),
        (BEACH, 'beach'),
        (INDOOR, 'indoor'),
    )
    SURFACE_NAMES = dict((k,v) for k,v in SURFACE_CHOICES)


    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    number_teams = models.PositiveSmallIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField()
    link = models.URLField(null=True, blank=True)
    surface = models.CharField(max_length=2,
                              choices=SURFACE_CHOICES,
                              default=GRASS)

    team = models.ManyToManyField(Team, through='TournamentTeam')

    def __unicode__(self):
        return self.name

    def get_surface(self):
        return self.SURFACE_NAMES[self.surface]



class TournamentTeam(models.Model):
    OPEN = 'O'
    MIXED = 'M'
    WOMEN = 'W'
    DIVISION_CHOICES = (
        (OPEN, 'open'),
        (MIXED, 'mixed'),
        (WOMEN, 'women'),
    )

    team = models.ForeignKey(Team)
    tournament = models.ForeignKey(Tournament)
    div = models.CharField(max_length=2,
                           choices=DIVISION_CHOICES,
                           default=OPEN)

    seed = models.PositiveSmallIntegerField(null=True, blank=True)
    final_rank = models.PositiveSmallIntegerField(null=True, blank=True)
    spirit_rank = models.PositiveSmallIntegerField(null=True, blank=True)
    roster = models.ManyToManyField(Person)

    def __unicode__(self):
        return u'{0} {1}'.format(self.team, self.tournament)

