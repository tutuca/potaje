from django.contrib import admin
from albums.models import Album, Section, Content, HomeReel


class ContentInLine(admin.TabularInline):
    model = Content
    extra = 1
    fields = ('source', 'image', 'caption',)


class ContentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'caption', 'kind', 'album', 'created')
    list_filter = ('album', 'kind')


class AlbumAdmin(admin.ModelAdmin):
    inlines = [ContentInLine]
    list_display = ('name', 'section', 'created')
    list_filter = ('section', )
    date_hierarchy = 'created'


admin.site.register(Album, AlbumAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Section)
admin.site.register(HomeReel)
