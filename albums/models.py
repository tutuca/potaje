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

    @property
    def cover(self):
        return self.content_set.all()[0]

    @models.permalink
    def get_absolute_url(self):
        return ('album', (self.pk, ), )

    def __str__(self):
        return self.name


class Content(models.Model):
    caption = models.CharField(max_length=128, null=True, blank=True)
    album = models.ForeignKey('Album')
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True

    @property
    def html(self):
        raise NotImplemented


class Video(Content):
    source = models.URLField()
    thumbnail = models.URLField(editable=False)
    html = models.TextField(editable=False)

    def __str__(self):
        return self.thumbnail

    def save(self, *args, **kwargs):
        target = "http://vimeo.com/api/oembed.json?url=%s')" % self.source_url
        response = requests.get(target)
        data = json.loads(response.text)
        self.thumbnail = data['thumbnail_url']
        self.html = data['html']
        super(Video, self).save(*args, **kwargs)


class Picture(Content):
    image = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.image.url

    @property
    def html(self):
        return '<img src="%s" alt="%s" />' % (self.image.url, self.caption)
