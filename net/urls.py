from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import redirect

from net.views import generic_view, profile, test_login


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', lambda x: redirect('/login')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login', test_login),

    url(r'^account', generic_view('account')),
    url(r'^edit_profile', generic_view('edit_profile')),
    url(r'^feed', generic_view('feed')),
    url(r'^profile/(?P<pk>[\w-]+)$', profile),
)
