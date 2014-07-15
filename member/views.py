from django.views.generic import ListView, DetailView
from django.shortcuts import redirect

from member.models import Person, MemberJob

class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person


def my_detail(request):
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        return redirect('member:detail', pk=request.user.profile.pk)
    else:
        return redirect('member:list')