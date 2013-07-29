from website.models import Session, Speaker
from django.views.generic.list import ListView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import serializers

class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker

class SessionSerializer(serializers.ModelSerializer):
    speakers = SpeakerSerializer()

    class Meta:
        model = Session

class IndexView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Session.objects.all()

class SessionAPIListView(ListCreateAPIView):
    model = Session
    serializer_class = SessionSerializer

class SessionAPIRetrieveView(RetrieveUpdateAPIView):
    model = Session
    serializer_class = SessionSerializer
