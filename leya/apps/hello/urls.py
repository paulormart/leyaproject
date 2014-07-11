from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',

        url(r'^create/$', HelloCreateView.as_view(), name='create'),
        url(r'^list/$', HelloListView.as_view(), name='list'),
        url(r'^delete/(?P<pk>[0-9]+)/$', HelloRemoveView.as_view(), name='remove'),

)
