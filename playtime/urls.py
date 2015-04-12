from django.conf.urls import *

from playtime import views

urlpatterns = patterns('playtime.views',
  (r'^', views.PlaytimeHomeView.as_view()),
)
