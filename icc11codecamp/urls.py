from django.conf.urls import patterns, include, url
from website.views import IndexView, SessionAPIListView, SessionAPIRetrieveView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^api/sessions/$', SessionAPIListView.as_view(), name='list'),
    url(r'^api/sessions/(?P<pk>\d+)/$', SessionAPIRetrieveView.as_view(), name='retrieve'),
)
