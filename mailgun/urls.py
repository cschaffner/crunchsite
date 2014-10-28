from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from mailgun import views

urlpatterns = patterns('',
    url(r'^callback/$', views.callback, name='callback'),
)
