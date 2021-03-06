from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from .views import LandingPageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'leya.views.home', name='home'),
    url(r'^$', LandingPageView.as_view(), name='landing_page'),

    # url(r'^leyaproject/', include('leyaproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^hello/', include('leya.apps.hello.urls', namespace='hello', app_name='hello')),
)
