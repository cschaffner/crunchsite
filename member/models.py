from django.db import models
from django_iban.fields import IBANField, SWIFTBICField


class MemberStatus(models.Model):
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return self.status


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_thing = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(blank=True, null=True)
    iban = IBANField(blank=True, null=True)
    swift_bic = SWIFTBICField(blank=True, null=True)

    status = models.ForeignKey(MemberStatus)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.first_name, self.middle_thing, self.last_name)

