from django.db import models
from django.core import validators


class MailinglistAddressField(models.EmailField):
    """
    model field for email address that corresponds with a mailinglist on Mailgun
    """
    default_validators = [validators.validate_email]
    description = ("Mailinglist address")

    def formfield(self, **kwargs):
        # As with CharField, this will cause email validation to be performed
        # twice.
        defaults = {
            'form_class': forms.EmailField,
        }
        defaults.update(kwargs)
        return super(EmailField, self).formfield(**defaults)

