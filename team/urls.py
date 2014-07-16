from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from team import views

urlpatterns = patterns('',
    url(r'^$', views.TeamListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.TeamDetailView.as_view(), name='team_detail'),
    url(r'^tournament_team/(?P<pk>\d+)/$', views.TournamentTeamDetailView.as_view(), name='tournamentteam_detail'),
    url(r'^competition_team/(?P<pk>\d+)/$', views.CompetitionTeamDetailView.as_view(), name='competitionteam_detail'),
    # url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)/$', cache_page(60 * 15)(views.public_detail_team), name='detail'),
    # url(r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)/(?P<edit_key>\w+)/$', views.private_detail_team, name='private_detail'),
    # url(r'^edit/(?P<team_id>\d+)/(?P<edit_key>\w+)/$', views.edit, name='edit'),
    # url(r'^register/$', views.register_team, name='register'),
    # url(r'^stats/$', views.stats, name='stats'),
    # url(r'^thanks/(?P<team_id>\d+)/$', views.thanks, name='thanks'),
    # url(r'^confirm_email/(?P<confirmation_key>\w+)/$', views.confirm_email, name='confirm_email'),
    # url(r'^ajax_historic_team/$', views.ajax_historic_team, name='ajax_historic_team'),
    # url(r'^ajax_historic_division/$', views.ajax_historic_division, name='ajax_historic_division'),
)
