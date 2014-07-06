import json
import requests

from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=60)
    section = models.ForeignKey('Section')
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def cover(self):
        content = self.content_set.all()[0]
        if content:
            return content.thumbnail

    @models.permalink
    def get_absolute_url(self):
        return ('album', (self.pk, ), )

    def __str__(self):
        return self.name


class Content(models.Model):
    caption = models.CharField(max_length=128, null=True, blank=True)
    album = models.ForeignKey('Album')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    thumbnail = models.URLField(editable=False)
    code = models.TextField(editable=False)

    def __str__(self):
        return self.caption


class Video(Content):
    source = models.URLField()

    def save(self, *args, **kwargs):
        target = "http://vimeo.com/api/oembed.json?url=%s" % self.source
        response = requests.get(target)
        data = json.loads(response.text)
        self.caption = data['title']
        self.thumbnail = data['thumbnail_url']
        self.code = data['html']
        super(Video, self).save(*args, **kwargs)

    @property
    def html(self):
        return super(Picture, self).html(self.code)


class Picture(Content):
    image = models.ImageField(upload_to='pictures')

    def save(self, *args, **kwargs):
        self.thumbnail = self.image.url
        self.code = '<img src="%s" alt="%s" />' % (self.image.url, self.caption)
        super(Picture, self).save(*args, **kwargs)

