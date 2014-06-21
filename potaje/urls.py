from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.sitemaps import GenericSitemap
from albums.models import Album
admin.autodiscover()

info_dict = {
    'queryset': Album.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'leaks': GenericSitemap(info_dict, priority=0.6),
}


urlpatterns = patterns('albums.views',
    url(r'^$', 'home', name='home'),
    url(r'^album/(?P<id>\d+)$', 'album', name='album'),
    url(r'^about/$', 'about', name='about'),
)

urlpatterns += patterns('',
    url(r'^lobby/', include(admin.site.urls)),
    (r'^robots\.txt$', lambda r: HttpResponse(
        "User-agent: *\nDisallow: /media/*\nDisallow: /lobby/*", mimetype="text/plain")),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', 
        {'sitemaps': sitemaps})

)
