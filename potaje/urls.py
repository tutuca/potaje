from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.sitemaps import GenericSitemap
from django.conf.urls.static import static
from django.conf import settings
from albums.models import Album
from albums import views
from albums.resources import AlbumResource, SectionResource

admin.autodiscover()

info_dict = {
    'queryset': Album.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'potaje': GenericSitemap(info_dict, priority=0.6),
}


urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
)
urlpatterns += patterns(
    '',
    url(r'api/', include(SectionResource.urls())),
    url(r'api/album/', include(AlbumResource.urls())),

)
urlpatterns += patterns(
    '',
    url(r'^lobby/', include(admin.site.urls)),
    (r'^robots\.txt$', lambda r: HttpResponse(
        "User-agent: *\nDisallow: /media/*\nDisallow: /lobby/*", mimetype="text/plain")),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps})

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
