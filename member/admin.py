from django.contrib import admin
from member.models import Person, MemberJob
from cms.admin.placeholderadmin import PlaceholderAdminMixin

class PersonAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ('first_name', 'middle_thing', 'last_name', 'jobs')
    # list_filter = ('jobs', )
    def jobs(self, instance):
        return instance.jobs.all()

#
# class TeamAdmin(admin.ModelAdmin):
#     pass
#     # list_display = ('name', 'division', 'status', 'final_rank', 'groupme_bot_id', 'groupme_share_url', 'num_players', 'num_guests')
#     # list_filter = ['division', 'status']
#     # list_editable = ['final_rank', 'groupme_bot_id', 'groupme_share_url']
#     #
#     # actions = ['upload_to_leaguevine_as_test', 'update_seed_as_test', 'upload_to_leaguevine', 'update_seed',
#     #            'groupme_create_group', 'groupme_create_bot', 'update_groupme_bot_id']
#     #
#     # def get_lv_standing(modeladmin, request, queryset):
#     #     for team in queryset:
#     #         if team.leaguevine_id:
#     #             # TODO: it's too much effort right now, enter ranks manually!
#     #             pass
#

admin.site.register(Person, PersonAdmin)
admin.site.register(MemberJob)
