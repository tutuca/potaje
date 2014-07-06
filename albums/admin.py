from django.contrib import admin
from albums.models import Album, Picture, Video, Section


class PictureInLine(admin.TabularInline):
    model = Picture
    extra = 1
    fields = ('image', 'caption', )

class VideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('source', 'caption',)


class PictureAdmin(admin.ModelAdmin):
    list_display = ('image', 'album', 'created')
    list_filter = ('album', )


class AlbumAdmin(admin.ModelAdmin):
    inlines = [PictureInLine, VideoInLine]
    list_display = ('name', 'section', 'created')
    list_filter = ('section', )


admin.site.register(Album, AlbumAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Section)
