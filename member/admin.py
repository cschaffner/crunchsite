from django.contrib import admin
from member.models import Person, MemberJob, Job
from team.admin import TeamMemberInline
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from import_export.admin import ImportExportMixin
from import_export.resources import ModelResource
from import_export import fields
from mailgun.admin import EmailInlineJob
import autocomplete_light

class PersonResource(ModelResource):
    # playing_level = fields.Field()
    # teams = fields.Field()

    class Meta:
        model = Person
        exclude = ('description', )
        # widgets = {
        #         'birthday': {'format': '%d.%m.%Y'},
        #         }

    # def dehydrate_teams(self, person):
    #     assert isinstance(person.team_set, object)
    #     return list(person.team_set.values_list('pk', flat=True))



class MemberJobAdmin(admin.ModelAdmin):
    model = MemberJob
    form = autocomplete_light.modelform_factory(MemberJob)

#
#
# class MemberJobInline(admin.TabularInline):
#     model = MemberJob
#     form = autocomplete_light.modelform_factory(MemberJob)
#

class JobAdmin(admin.ModelAdmin):
    model = Job
    inlines = [
        EmailInlineJob,
    ]


class PersonAdmin(PlaceholderAdminMixin, ImportExportMixin, admin.ModelAdmin):
    resource_class = PersonResource
    list_display = ('__unicode__', 'gender', 'playing_level')
    list_filter = ('gender', 'playing_level')
    # inlines = [
    #     TeamMemberInline,
    #     MemberJobInline
    # ]
    form = autocomplete_light.modelform_factory(Person)

    def jobs(self, instance):
        return instance.jobs.all()


admin.site.register(Job, JobAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(MemberJob, MemberJobAdmin)
