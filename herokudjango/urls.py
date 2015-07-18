from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'herokudjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Applications
    url(r'^', include('foe.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Registration
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
