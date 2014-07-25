from django.contrib import admin
from team.models import Team, Tournament, TournamentTeam, TeamMember, CompetitionTeam, Competition, \
                                TournamentTeamMember, CompetitionTeamMember
from member.models import Person
from cms.admin.placeholderadmin import PlaceholderAdminMixin
import autocomplete_light

class TournamentAdmin(admin.ModelAdmin):
    pass

class CompetitionAdmin(admin.ModelAdmin):
    pass

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    form = autocomplete_light.modelform_factory(TeamMember)

class TournamentTeamMemberInline(admin.TabularInline):
    model = TournamentTeamMember
    form = autocomplete_light.modelform_factory(TournamentTeamMember)

class CompetitionTeamMemberInline(admin.TabularInline):
    model = CompetitionTeamMember
    form = autocomplete_light.modelform_factory(CompetitionTeamMember)



class TeamAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    actions = ['create_email_list', 'add_team_members_to_mailinglist']
    inlines = [
        TeamMemberInline
    ]

    def create_email_list(modeladmin, request, queryset):
        for team in queryset:
            team.create_mailinglist()

    def add_team_members_to_mailinglist(modeladmin, request, queryset):
        for team in queryset:
            team.add_team_members_to_mailinglist()


class TournamentTeamAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    actions = ['import_team_roster']
    inlines = [
        TournamentTeamMemberInline
    ]

    def import_team_roster(modeladmin, request, queryset):
        for tournament_team in queryset:
            tournament_team.import_team_roster()

class CompetitionTeamAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    actions = ['import_team_roster']
    inlines = [
        CompetitionTeamMemberInline
    ]

    def import_team_roster(modeladmin, request, queryset):
        for competition_team in queryset:
            competition_team.import_team_roster()

    import_team_roster.short_description = 'Imports team roster from team into competionteam'

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'team', 'status')
    list_filter = ['team']
    form = autocomplete_light.modelform_factory(TeamMember)


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
