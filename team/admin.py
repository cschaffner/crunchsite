from django.contrib import admin
from team.models import Team, Tournament, TournamentTeam, TeamMember, CompetitionTeam, Competition, \
                                TournamentTeamMember, CompetitionTeamMember
from cms.admin.placeholderadmin import PlaceholderAdminMixin

class TournamentAdmin(admin.ModelAdmin):
    pass

class CompetitionAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

class TournamentTeamAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

class CompetitionTeamAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'team', 'status')
    list_filter = ['team']
    # list_editable = ['final_rank', 'groupme_bot_id', 'groupme_share_url']
    #
    # actions = ['upload_to_leaguevine_as_test', 'update_seed_as_test', 'upload_to_leaguevine', 'update_seed',
    #            'groupme_create_group', 'groupme_create_bot', 'update_groupme_bot_id']
    #
    # def get_lv_standing(modeladmin, request, queryset):
    #     for team in queryset:
    #         if team.leaguevine_id:
    #             # TODO: it's too much effort right now, enter ranks manually!
    #             pass

class TournamentTeamMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'tournamentteam', 'status')
    list_filter = ['tournamentteam']


class CompetitionTeamMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'competitionteam', 'status')
    list_filter = ['competitionteam']


admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(TournamentTeamMember, TournamentTeamMemberAdmin)
admin.site.register(CompetitionTeamMember, CompetitionTeamMemberAdmin)
admin.site.register(TournamentTeam, TournamentTeamAdmin)
admin.site.register(CompetitionTeam, CompetitionTeamAdmin)
