from django.db import models
from django.core.urlresolvers import reverse

from member.models import Person
from django_countries.fields import CountryField
from cms.models.fields import PlaceholderField


def my_report_slotname(instance):
    return 'tournament_report'

def my_competition_day1_slotname(instance):
    return 'competition_day1_report'

def my_competition_day2_slotname(instance):
    return 'competition_day2_report'

def my_competition_day3_slotname(instance):
    return 'competition_day3_report'

def my_competition_day4_slotname(instance):
    return 'competition_day4_report'

def my_team_slotname(instance):
    return 'team_description'


class Team(models.Model):
    name = models.CharField(max_length=100)
    roster = models.ManyToManyField(Person, through='TeamMember')
    description = PlaceholderField(my_team_slotname)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team:team_detail', args=[self.pk])


class TeamMember(models.Model):
    CAPTAIN = '1CA'
    PLAYER = '2PL'
    PRACTICE = '3PR'
    TRAINER = '4TR'
    COACH = '5CO'
    ALUMNI = '9AL'
    STATUS_CHOICES = (
        (CAPTAIN, 'captain'),
        (PLAYER, 'player'),
        (PRACTICE, 'practice only'),
        (TRAINER, 'trainer'),
        (COACH, 'coach'),
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

    class Meta:
        ordering = ['status', 'member__last_name']
        unique_together = ['team', 'member']


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

    class Meta:
        ordering = ['start_date']

    def __unicode__(self):
        return self.name


class Competition(models.Model):
    OPEN = '1O'
    MIXED = '2M'
    WOMEN = '3W'
    DIVISION_CHOICES = (
        (OPEN, 'open'),
        (MIXED, 'mixed'),
        (WOMEN, 'women'),
    )
    div = models.CharField(max_length=2,
                           choices=DIVISION_CHOICES,
                           default=OPEN)

    number_divisions = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Number of Divisions')
    number_teams = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Number of Teams')

    day1 = models.DateField() # there should be at least one competition day
    day2 = models.DateField(blank=True, null=True)
    day3 = models.DateField(blank=True, null=True)
    day4 = models.DateField(blank=True, null=True)

    day1_lv_id = models.IntegerField(blank=True, null=True)
    day2_lv_id = models.IntegerField(blank=True, null=True)
    day3_lv_id = models.IntegerField(blank=True, null=True)
    day4_lv_id = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['day1']

    def __unicode__(self):
        return u'{0} competition {1}'.format(self.get_div_display(), self.day1.year)


class CompetitionTeam(models.Model):
    team = models.ForeignKey(Team)
    competition = models.ForeignKey(Competition)
    competition_name = models.CharField(max_length=100,
                                        verbose_name='Competition Team Name',
                                        blank=True, null=True)

    seed = models.PositiveSmallIntegerField(null=True, blank=True)
    final_rank = models.PositiveSmallIntegerField(null=True, blank=True)
    spirit_rank = models.PositiveSmallIntegerField(null=True, blank=True)
    roster = models.ManyToManyField(Person, through='CompetitionTeamMember')

    report_day1 = PlaceholderField(my_competition_day1_slotname, related_name='report_day1')
    report_day2 = PlaceholderField(my_competition_day2_slotname, related_name='report_day2')
    report_day3 = PlaceholderField(my_competition_day3_slotname, related_name='report_day3')
    report_day4 = PlaceholderField(my_competition_day4_slotname, related_name='report_day4')


    def __unicode__(self):
        if self.competition_name:
            return u'{0} @{1}'.format(self.competition_name, self.competition)
        else:
            return u'{0} @{1}'.format(self.team, self.competition)

    def get_absolute_url(self):
        return reverse('team:competitionteam_detail', args=[self.pk])


    def import_team_roster(self):
        """
        if roster is of competition team is still empty
        copies team roster from team to this competitionteam
        """
        if self.roster.count() == 0:
            for team_member in self.team.teammember_set.all():
                if team_member.status != TeamMember.ALUMNI and team_member.status != TeamMember.PRACTICE:
                    competitionteam_member = CompetitionTeamMember(competitionteam=self,
                                                                   member=team_member.member,
                                                                   status=team_member.status)
                    competitionteam_member.save()
        return True

    def save(self, *args, **kwargs):
        if not self.id:
            # newly created object, so set a flag
            first_time = True
        super(CompetitionTeam, self).save(*args, **kwargs)
        if first_time:
            # import team roster by default
            self.import_team_roster()


class TournamentTeam(models.Model):
    OPEN = '1O'
    MIXED = '2M'
    WOMEN = '3W'
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
    roster = models.ManyToManyField(Person, through='TournamentTeamMember')

    report = PlaceholderField(my_report_slotname)


    def __unicode__(self):
        return u'{0} @{1}'.format(self.team, self.tournament)

    def get_absolute_url(self):
        return reverse('team:tournamentteam_detail', args=[self.pk])

    def import_team_roster(self):
        """
        if roster is of competition team is still empty
        copies team roster from team to this competitionteam
        """
        if self.roster.count() == 0:
            for team_member in self.team.teammember_set.all():
                if team_member.status != TeamMember.ALUMNI and team_member.status != TeamMember.PRACTICE:
                    tournament_team = TournamentTeamMember(tournamentteam=self,
                                                           member=team_member.member,
                                                           status=team_member.status)
                    tournament_team.save()
        return True

    def save(self, *args, **kwargs):
        if not self.id:
            # newly created object, so set a flag
            first_time = True
        super(TournamentTeam, self).save(*args, **kwargs)
        if first_time:
            # import team roster by default
            self.import_team_roster()


class TournamentTeamMember(models.Model):
    CAPTAIN = '1CA'
    PLAYER = '2PL'
    PRACTICE = '3PR'
    TRAINER = '4TR'
    COACH = '5CO'
    STATUS_CHOICES = (
        (CAPTAIN, 'captain'),
        (PLAYER, 'player'),
        (PRACTICE, 'practice only'),
        (TRAINER, 'trainer'),
        (COACH, 'coach'),
    )
    STATUS_NAMES = dict((k,v) for k,v in STATUS_CHOICES)

    tournamentteam = models.ForeignKey(TournamentTeam)
    member = models.ForeignKey(Person)

    status = models.CharField(max_length=3,
                              choices=STATUS_CHOICES,
                              default=PLAYER)

    def __unicode__(self):
        return u'{1} ({0} of {2})'.format(self.STATUS_NAMES[self.status], self.member, self.tournamentteam)

    class Meta:
        ordering = ['status', 'member__last_name']
        unique_together = ['tournamentteam', 'member']


class CompetitionTeamMember(models.Model):
    CAPTAIN = '1CA'
    PLAYER = '2PL'
    PRACTICE = '3PR'
    TRAINER = '4TR'
    COACH = '5CO'
    STATUS_CHOICES = (
        (CAPTAIN, 'captain'),
        (PLAYER, 'player'),
        (PRACTICE, 'practice only'),
        (TRAINER, 'trainer'),
        (COACH, 'coach'),
    )
    STATUS_NAMES = dict((k,v) for k,v in STATUS_CHOICES)

    competitionteam = models.ForeignKey(CompetitionTeam)
    member = models.ForeignKey(Person)

    status = models.CharField(max_length=3,
                              choices=STATUS_CHOICES,
                              default=PLAYER)

    def __unicode__(self):
        return u'{1} ({0} of {2})'.format(self.STATUS_NAMES[self.status], self.member, self.competitionteam)

    class Meta:
        ordering = ['status', 'member__last_name']
        unique_together = ['competitionteam', 'member']

