from django.conf.urls import patterns, include, url
from django.contrib import admin

from net.friends.api.v1.routes import router

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'net.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/v1/', include(router.urls)),
)
