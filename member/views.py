from django.views.generic import ListView, DetailView
from member.models import Person, MemberJob


class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person