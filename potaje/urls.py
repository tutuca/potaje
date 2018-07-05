from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from albums.models import Album
from albums import views
from albums.resources import AlbumResource, SectionResource
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

info_dict = {
    'queryset': Album.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'potaje': GenericSitemap(info_dict, priority=0.6),
}


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^album/(?P<id>\d+)$', views.album, name='album'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    url(r'api/', SectionResource.urls),
    url(r'api/album/', AlbumResource.urls),
]

urlpatterns += [
    url(r'^lobby/', admin.site.urls),
    url(r'^robots\.txt$', lambda r: HttpResponse(
        "User-agent: *\nDisallow: /media/*\nDisallow: /lobby/*",
        mimetype="text/plain")),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')

]
