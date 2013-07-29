from website.models import Session, Speaker
from django.views.generic.list import ListView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import serializers

class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker

class SessionSerializer(serializers.ModelSerializer):
    speakers = SpeakerSerializer()
    both = serializers.SerializerMethodField("get_both")

    class Meta:
        model = Session
        fields = ('id', 'title', 'speakers', 'both', )

    def get_both(self, obj):
        return "yo"

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
