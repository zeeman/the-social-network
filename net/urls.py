from django.conf.urls import patterns, include, url
from django.contrib import admin

from net.views import basic_view


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'net.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/', basic_view('account')),
    url(r'^feed/', basic_view('feed')),
    url(r'^profile/', basic_view('profile')),
)
