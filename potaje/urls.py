from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('albums.views',
    url(r'^$', 'home', name='home'),
    url(r'^album/(?P<id>\d+)$', 'album', name='album'),
    url(r'^about/$', 'about', name='about'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
