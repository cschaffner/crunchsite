from django.contrib import admin, messages
from models import Email
import requests

class EmailInlineJob(admin.TabularInline):
    model = Email
    fields = ('email', 'description')

class EmailInlineTeam(admin.TabularInline):
    model = Email
    fields = ('email', 'description')

class EmailAdmin(admin.ModelAdmin):
    actions = ['sync_mailgun']
    model = Email

    def sync_mailgun(self, request, queryset):
        for email in queryset:
            response = email.sync_mailgun()
            if response.status_code == requests.codes.OK:
                self.message_user(request, u'{0}: {1}'.format(email, response.content))
            else:
                self.message_user(request, u'{0}: {1}'.format(email, response.content), level=messages.ERROR)
    sync_mailgun.short_description = 'Sync with Mailgun'

admin.site.register(Email, EmailAdmin)

