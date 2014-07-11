from django.views.generic import ListView, DetailView

from team.models import Team, TournamentTeam

class TeamListView(ListView):
    model = Team

    # def get_context_data(self, **kwargs):
    #     context = super(PredictionListView, self).get_context_data(**kwargs)
    #     context['averages'] = Prediction.objects.averages()
    #     context['num_predictions'] = Prediction.objects.all().count()
    #     return context

class TeamDetailView(DetailView):
    model = Team


class TournamentTeamDetailView(DetailView):
    model = TournamentTeam

