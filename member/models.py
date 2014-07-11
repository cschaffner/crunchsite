from django.db import models
from django_iban.fields import IBANField, SWIFTBICField
from django.core.exceptions import ValidationError


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_thing = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(blank=True, null=True)
    iban = IBANField(blank=True, null=True)
    swift_bic = SWIFTBICField(blank=True, null=True)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.first_name, self.middle_thing, self.last_name)

    class Meta:
        ordering = ['last_name']

    # def clean(self):
    #     # every person needs at least one job
    #     # TODO: Let's wait until we know more about the business logic
    #
    #     if self.jobs.count() == 0:
    #         raise ValidationError('Every person needs at least one job!')


class MemberJob(models.Model):
    PLAYER = '1PL'
    CHAIRMAN = '2CH'
    TREASURER = '3TR'
    SECRETARY = '4SE'
    COMPETITION = '5CO'
    GENERAL = '6GE'
    YOUTH = '7YO'
    ALUMNI = '99A'
    JOB_CHOICE = (
        (PLAYER, u'active player'),
        (CHAIRMAN, u'chairman (bestuur)'),
        (TREASURER, u'treasurer (bestuur)'),
        (SECRETARY, u'secretary (bestuur)'),
        (COMPETITION, u'competition officer (bestuur)'),
        (GENERAL, u'general board member (bestuur)'),
        (YOUTH, u'youth coordinator (bestuur)'),
        (ALUMNI, u'alumni'),
    )
    job = models.CharField(max_length=3, choices=JOB_CHOICE, default=PLAYER)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    person = models.ForeignKey(Person, related_name='jobs')

    def __unicode__(self):
        return self.get_job_display()
