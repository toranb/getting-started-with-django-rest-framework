from django.db import models

class Session(models.Model):
    title = models.CharField(max_length=25)

class Speaker(models.Model):
    name = models.CharField(max_length=50)
    session = models.ForeignKey(Session, related_name='speakers')
