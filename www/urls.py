from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

admin.autodiscover()

# #old site redirects
# urlpatterns = patterns('',
#
#     url(r'^2[0-9]*/teams/.*$', RedirectView.as_view(url='/tournament-info/team-selection/', permanent=True)),
#     url(r'^2[0-9]*/photosvideo/.*$', RedirectView.as_view(url='/the-media/photos/', permanent=True)),
#     url(r'^2[0-9]*/preregisterusa/.*$', RedirectView.as_view(url='/', permanent=True)),
#     url(r'^2[0-9]*/contact/.*$', RedirectView.as_view(url='/', permanent=True)),
#     url(r'^2[0-9]*/video/.*$', RedirectView.as_view(url='/the-media/video/', permanent=True)),
#     url(r'^2[0-9]*/tourney/.*$', RedirectView.as_view(url='/tournament-info/', permanent=True)),
#     url(r'^2[0-9]*/directions/.*$', RedirectView.as_view(url='/tournament-info/directions/', permanent=True)),
#     url(r'^2[0-9]*/news/.*$', RedirectView.as_view(url='/', permanent=True)),
#     url(r'^2[0-9]*/about/.*$', RedirectView.as_view(url='/about/', permanent=True)),
#     url(r'^2[0-9]*/green/.*$', RedirectView.as_view(url='/about/green-windmill/', permanent=True)),
#     url(r'^2[0-9]*/charity/.*$', RedirectView.as_view(url='/', permanent=True)),
#     url(r'^2[0-9]*/history/.*$', RedirectView.as_view(url='/about/history/', permanent=True)),
#     url(r'^2[0-9]*/sponsors/.*$', RedirectView.as_view(url='/about/sponsors/', permanent=True)),
#     url(r'^2[0-9]*/crew/.*$', RedirectView.as_view(url='/about/crew/', permanent=True)),
#     url(r'^2[0-9]*/volunteers/.*$', RedirectView.as_view(url='/', permanent=True)),
#     url(r'^2[0-9]*/pickup/.*$', RedirectView.as_view(url='/teams/pickup', permanent=True)),
#     url(r'^2[0-9]*/eventschedule/.*$', RedirectView.as_view(url='/event/event-schedule', permanent=True)),
#     url(r'^2[0-9]*/rulesandformat/.*$', RedirectView.as_view(url='/tournament-info/rules-and-format', permanent=True)),
#     url(r'^2[0-9]*/wherehasyourgearbeen/.*$', RedirectView.as_view(url='/about/windmill-gear', permanent=True)),
#     url(r'^2[0-9]*/amsterdam/.*$', RedirectView.as_view(url='/about/amsterdam', permanent=True)),
#     url(r'^2[0-9]*/press/.*$', RedirectView.as_view(url='/the-media/press', permanent=True)),
#     url(r'^2[0-9]*/.*$', RedirectView.as_view(url='/', permanent=True)),
# )


urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^news/', include('zinnia.urls')),
    # url(r'^forms/', include('form_designer.urls')),
    # url(r'^captcha/', include('captcha.urls')),
    # url(r'^groupme/', include('groupme.urls')),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^', include('cms.urls')),
)

#favicon and robots.txt shut mail up patterns
urlpatterns += patterns('',
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt")),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/website/favicon.ico'))
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
  ) + urlpatterns


# urlpatterns += patterns('', (
#         r'^static/(?P<path>.*)$',
#         'django.views.static.serve',
#         {'document_root': 'static'}
# ))

