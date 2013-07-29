from website.models import Session
from django.views.generic.list import ListView

class IndexView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Session.objects.all()
