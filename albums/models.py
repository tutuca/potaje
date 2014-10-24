import json
import requests

from urllib import parse

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
        content = self.content_set.first()
        if content:
            return content.thumbnail

    @models.permalink
    def get_absolute_url(self):
        return ('album', (self.pk, ), )

    def __str__(self):
        return self.name


class Content(models.Model):
    source = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    kind = models.SmallIntegerField(
        choices=(
            (10, 'Picture'),
            (20, 'Video'),
        ),
        default=10
    )
    caption = models.CharField(max_length=128, null=True, blank=True)
    album = models.ForeignKey('Album')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    thumbnail = models.URLField(editable=False)
    code = models.TextField(editable=False)

    def save(self, *args, **kwargs):
        if self.image:
            self.caption = self.caption or self.image.name
            self.kind = 10
            self.thumbnail = self.image.url
            self.code = '<img src="%s" alt="%s" />' % (
                self.image.url, self.caption)

        if "imgur" in self.source:
            old_code = self.source
            split = parse.urlsplit(self.source)
            img_id = split.path[1:]  # sacamos el primer /
            if any(x in split.path for x in ('.gif', '.jpg', '.png',)):
                # es una imágen directa, sacamos la extensión
                img_id = img_id[:-4]

            self.kind = 10
            self.caption = old_code
            self.thumbnail = "http://i.imgur.com/%st.jpg" % img_id
            self.code = '<img src="http://i.imgur.com/%s.jpg" alt="%s" />' % (
                img_id, self.caption)

        if "vimeo" in self.source:
            options = {
                "url": self.source,
                "&portrait": 0,
                "title": 0,
                "byline": 0,
            }
            target = "http://vimeo.com/api/oembed.json?%s" % parse.urlencode(
                options
            )
            response = requests.get(target)
            data = json.loads(response.text)

            self.kind = 20
            self.caption = data['title']
            self.thumbnail = data['thumbnail_url']
            self.code = data['html']

        super(Content, self).save(*args, **kwargs)
