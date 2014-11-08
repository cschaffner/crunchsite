from django.db import models
from www import settings
from django.core.exceptions import ValidationError
import requests
import json

class Email(models.Model):
    email = models.EmailField(unique=True, help_text='emails to this address will be forwarded')
    description = models.CharField(max_length=50, blank=True, null=True)
    list = models.BooleanField(default=False, help_text='address stands for an email list')
    job = models.ForeignKey('member.Job', blank=True, null=True)
    team = models.OneToOneField('team.Team', blank=True, null=True)

    def __unicode__(self):
        return self.email

    def clean(self):
        # self.email has to end in settings.MAILGUN_DOMAIN
        if self.email and self.email[-len(settings.MAILGUN_DOMAIN):] != settings.MAILGUN_DOMAIN:
            raise ValidationError('Email addresses have to end in {0}'.format(settings.MAILGUN_DOMAIN))


    def sync_mailgun(self):
        """
        returns a requests.Response() object
        with status_code = 600 in case of ConnectionError to mailgun
        with status_code = 200 if successfully synced with mailgun

        """
        response = requests.Response()
        response.status_code = 200
        if self.team:
            # Remove mailing list with this address from Mailgun
            try:
                r = requests.delete(
                    "https://api.mailgun.net/v2/lists/{0}".format(self.email),
                    auth=('api', settings.MAILGUN_API_KEY))
            except requests.ConnectionError:
                response.status_code = 600
                response._content = u'could not connect to Mailgun'
                return response

            # create a new one
            try:
                r = requests.post(
                    "https://api.mailgun.net/v2/lists",
                    auth=('api', settings.MAILGUN_API_KEY),
                    data={'address': '{0}'.format(self.email),
                          'name': '{0}'.format(self.team.name),
                          'description': "mailing list for team {0}".format(self.team.name)})
            except requests.ConnectionError:
                response.status_code = 600
                response._content = u'could not connect to Mailgun'
                return response

            # get email addresses and names of players of this team
            if self.team.teammember_set.count() > 0:
                members = []
                for teammember in self.team.teammember_set.all():
                    members.append({
                        'address': '{0} <{1}>'.format(teammember.member, teammember.member.email),
                        'vars': {'gender': teammember.member.get_gender_display()},
                    })

                # add these members to mailing list
                try:
                    r = requests.post(
                        "https://api.mailgun.net/v2/lists/{0}/members.json".format(self.email),
                        auth=('api', settings.MAILGUN_API_KEY),
                        data={'subscribed': True,
                              'members': json.dumps(members)},
                    )
                except requests.ConnectionError:
                    response.status_code = 600
                    response._content = u'could not connect to Mailgun'
                    return response

            response._content = u'team email list synced with Mailgun'
            return response
        else: # jobs
             # figure out the destinations for this job
            actions = []
            if self.job.person_set.count() == 0:
                # no person assigned to this job
                # forward to info@DOMAIN instead
                actions.append("forward('info@{0}')".format(settings.MAILGUN_DOMAIN))
            else:
                for person in self.job.person_set.all():
                    actions.append("forward('{0}')".format(person.email))
            actions.append("stop()")


             # create a new route
            try:
                r = requests.post(
                    "https://api.mailgun.net/v2/routes",
                    auth=('api', settings.MAILGUN_API_KEY),
                    data={'priority': 100,
                          'description': '{0}'.format(self.job.description),
                          'expression': "match_recipient('{0}')".format(self.email),
                          'action': actions})
            except requests.ConnectionError:
                response.status_code = 600
                response._content = u'could not connect to Mailgun'
                return response

            response._content = u'job email address synced with Mailgun'
            return response


    # def clean(self):
    #
    #     # check if mailinglist_address will be changed
    #     if self.mailinglist_address is not None:
    #         old_address = None
    #         if self.id:
    #             old_address = Team.objects.get(pk=self.id).mailinglist_address
    #
    #         if self.mailinglist_address != old_address:
    #             response = self.update_mailinglist_address(old_address)
    #             if response.status_code >= 400 or response.json()['address'] != self.mailinglist_address:
    #                 self.mailinglist_address = old_address
    #                 raise ValidationError('mailinglist adress could not been changed')
    #
    #
    #
    # # def save(self, *args, **kwargs):
    # #     super(Team, self).save(*args, **kwargs)
    # #
    # #
    #
    # def update_mailinglist_address(self, old_address=None):
    #     """
    #     returns a requests.Response() object
    #     with status_code = 600 in case of ConnectionError to mailgun
    #     with status_code = 200 if self.mailinglist_address is not set (nothing to do)
    #     with status_code = 200 if old_address == self.mailinglist (nothing to do)
    #
    #     if old_address is set, it updates the mailgun mailinglist old_address to self.mailinglist_address
    #     if old_address is not set, it creates a new mailgun mailinglist with address self.mailinglist_address
    #
    #     """
    #     response = requests.Response()
    #
    #     if not self.mailinglist_address:
    #         response.status_code = 200
    #         response._content = u'mailinglist_address not set'
    #         return response
    #
    #     if old_address == self.mailinglist_address:
    #         response.status_code = 200
    #         response._content = u'nothing to do'
    #         return response
    #
    #     if not old_address:
    #         # create mailinglist on mailgun
    #         try:
    #             response = requests.post(
    #                 "https://api.mailgun.net/v2/lists",
    #                 auth=('api', settings.MAILGUN_API_KEY),
    #                 data={'address': '{0}'.format(self.mailinglist_address),
    #                       'description': "{0} mailing list".format(self.name)})
    #         except requests.ConnectionError:
    #             response = requests.Response()
    #             response.status_code = 600
    #             response._content = u'could not connect to Mailgun'
    #     else:
    #         # update existing mailing list on mailgun
    #         try:
    #             #TODO: update instead!
    #             response = requests.post(
    #                 "https://api.mailgun.net/v2/lists",
    #                 auth=('api', settings.MAILGUN_API_KEY),
    #                 data={'address': '{0}'.format(self.mailinglist_address),
    #                       'description': "{0} mailing list".format(self.name)})
    #         except requests.ConnectionError:
    #             response = requests.Response()
    #             response.status_code = 600
    #             response._content = u'could not connect to Mailgun'
    #
    #     return response
    #
    #
    # def add_team_members_to_mailinglist(self):
    #     # collect teammembers to be added
    #     members = []
    #     for teammember in self.teammember_set.all():
    #         members.append({
    #             'address': '{0} <{1}>'.format(teammember.member, teammember.member.email),
    #             'vars': {'gender': teammember.member.get_gender_display()},
    #         })
    #     try:
    #         response = requests.post(
    #             "https://api.mailgun.net/v2/lists/{0}/members.json".format(self.mailinglist_address),
    #             auth=('api', settings.MAILGUN_API_KEY),
    #             data={'subscribed': True,
    #                   'members': json.dumps(members)},
    #         )
    #     except requests.ConnectionError:
    #         response = requests.Response()
    #         response.status_code = 600
    #         response._content = u'could not connect to Mailgun'
    #
    #     return response
