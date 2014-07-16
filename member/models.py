from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django_iban.fields import IBANField, SWIFTBICField
from cms.models.fields import PlaceholderField
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from django_countries.fields import CountryField
import hashlib

def my_member_slotname(instance):
    return 'member_description'

User.profile = property(lambda u: Person.objects.get_or_create(user=u)[0])

class Person(models.Model):
    MALE = '1M'
    FEMALE = '2F'
    GENDER_CHOICE = (
        (MALE, u'male'),
        (FEMALE, u'female'),
    )

    DONTKNOW = '1DN'
    BEGINNER = '2BG'
    INTERMEDIATE = '3IN'
    HIGH = '4HI'
    LEVEL_CHOICE = (
        (DONTKNOW, u"I don't know"),
        (BEGINNER, u'beginner'),
        (INTERMEDIATE, u'intermediate'),
        (HIGH, u'as high as possible'),
    )

    AGREE = '1OK'
    NOTAGREE = '2NO'
    AUTHORISATION_CHOICE = (
        (AGREE, u'I agree'),
        (NOTAGREE, u'I do not agree'),
    )

    NODISCOUNT = '1NO'
    STUDENT = '2ST'
    YOUTH = '3YO'
    DISCOUNT_CHOICE = (
        (NODISCOUNT, u'no discount'),
        (STUDENT, u'full-time student (not PhD/AiO)'),
        (YOUTH, u'youth'),
    )

    first_name = models.CharField(max_length=100)
    preposition = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICE,
                              default=MALE)
    playing_level = models.CharField(max_length=3,
                                     choices=LEVEL_CHOICE,
                                     default=DONTKNOW)
    street = models.CharField(max_length=200, blank=True, null=True)
    house_number = models.PositiveSmallIntegerField(blank=True, null=True)
    house_number_extension = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=7, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    citizenship = CountryField(blank=True, null=True)

    discount = models.CharField(max_length=3,
                                  choices=DISCOUNT_CHOICE,
                                  default=NODISCOUNT)
    iban_authorisation = models.CharField(max_length=3,
                                          choices=AUTHORISATION_CHOICE,
                                          default=AGREE)
    iban = IBANField(blank=True, null=True)
    account_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='bank account in the name of')

    email = models.EmailField(blank=True, null=True)


    user = models.OneToOneField(User, related_name='profile', blank=True, null=True)

    description = PlaceholderField(my_member_slotname)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.first_name, self.preposition, self.last_name)

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
