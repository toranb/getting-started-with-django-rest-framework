from website.models import Session
from django.views.generic.list import ListView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

class IndexView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Session.objects.all()

class SessionAPIListView(ListCreateAPIView):
    model = Session

class SessionAPIRetrieveView(RetrieveUpdateAPIView):
    model = Session
