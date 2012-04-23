from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'potaje.views.home', name='home'),
    url(r'^album/(?P<id>\d+)$', 'potaje.views.album', name='album'),
    url(r'^about/$', 'potaje.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
