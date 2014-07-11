from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',

        url(r'^create/$', CreateView.as_view(), name='hello_create'),
        url(r'^list/$', ListView.as_view(), name='hello__list'),

)
