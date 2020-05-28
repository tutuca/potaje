from django.urls import path
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
    "queryset": Album.objects.all(),
    "date_field": "created",
}

sitemaps = {
    "potaje": GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = [
    path("api/", SectionResource.urls),
    path("api/album/", AlbumResource.urls),
    path("album/<int:id>", views.album, name="album"),
    path("lobby/", admin.site.urls),
    path(
        "robots.txt",
        lambda r: HttpResponse(
            "User-agent: *\nDisallow: /media/*\nDisallow: /lobby/*",
            content_type="text/plain",
        ),
    ),
    path(
        "sitemap.xml",
        sitemap,
        kwargs={"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("", views.home, name="home"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
