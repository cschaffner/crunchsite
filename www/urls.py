from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import autocomplete_light
autocomplete_light.autodiscover()
admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^playtime/', include('playtime.urls')),
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


urlpatterns += patterns(
    '',
    url(r'^', include('cms.urls')),
)