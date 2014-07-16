from django.contrib import admin
from member.models import Person, MemberJob
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from import_export.admin import ImportExportMixin
from import_export.resources import ModelResource
from import_export import fields

class PersonResource(ModelResource):
    # playing_level = fields.Field()

    class Meta:
        model = Person
        exclude = ('description', )
        widgets = {
                'birthday': {'format': '%d.%m.%Y'},
                }

    # def dehydrate_playing_level(self, person):
    #     return u'{0}'.format(person.get_playing_level_display())


class PersonAdmin(PlaceholderAdminMixin, ImportExportMixin, admin.ModelAdmin):
    resource_class = PersonResource
    list_display = ('first_name', 'preposition', 'last_name', 'jobs')
    # list_filter = ('jobs', )
    def jobs(self, instance):
        return instance.jobs.all()



admin.site.register(Person, PersonAdmin)
admin.site.register(MemberJob)
