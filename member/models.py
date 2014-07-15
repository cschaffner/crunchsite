from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django_iban.fields import IBANField, SWIFTBICField
from cms.models.fields import PlaceholderField
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
import hashlib

def my_member_slotname(instance):
    return 'member_description'


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, related_name='example_profile')
#
#     def __unicode__(self):
#         return "{}'s profile".format(self.user.username)
#
#     class Meta:
#         db_table = 'user_profile'
#
#     def account_verified(self):
#         if self.user.is_authenticated:
#             result = EmailAddress.objects.filter(email=self.user.email)
#             if len(result):
#                 return result[0].verified
#         return False

User.profile = property(lambda u: Person.objects.get_or_create(user=u)[0])

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_thing = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(blank=True, null=True)
    iban = IBANField(blank=True, null=True)
    swift_bic = SWIFTBICField(blank=True, null=True)

    user = models.OneToOneField(User, related_name='profile', blank=True, null=True)

    description = PlaceholderField(my_member_slotname)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.first_name, self.middle_thing, self.last_name)

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        return reverse('member:detail', args=[self.pk])


    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())


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
