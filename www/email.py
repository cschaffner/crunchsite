from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

def send_email(subject, body, sender, recipients):
    if settings.EMAIL_TEST:
        send_email_test(subject, body, sender, recipients)
    else:
        email = EmailMessage(subject, body, sender, recipients)
        if settings.EMAIL_BCC:
            email.bcc.append(settings.EMAIL_BCC)
        return email.send()

def send_email_test(subject, body, sender, recipients):
    """ Sends emails addressed to users specified in the EMAIL_TEST_RECIPIENT variable specified in settings.py.

        EMAIL_TEST_RECIPIENT can be either a string or a list of strings representing one or
            more email addresses to send test emails to.
    """
    if isinstance(recipients, list):
        for recipient in recipients:
            detail_subject = u'[Test to {0}] {1}'.format(recipient, subject)
            send_mail(detail_subject, body, sender, settings.EMAIL_TEST_RECIPIENT)
    else:
        detail_subject = u'[Test to {0}] {1}'.format(recipients, subject)
        send_mail(detail_subject, body, sender, settings.EMAIL_TEST_RECIPIENT)
