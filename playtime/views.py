from django.views.generic import TemplateView


# Create your views here.
class PlaytimeHomeView(TemplateView):
    template_name = "playtime/home.html"
