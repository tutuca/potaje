import json
import requests

from urllib import parse

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Section(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    order = models.IntegerField()

    class Meta:
        ordering = ('order',)

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
    thumbnail = models.URLField(editable=False, default="")
    code = models.TextField(editable=False, default="")



@receiver(post_save, sender=Content)
def fetch_image(sender, instance, **kwargs):
    if instance.thumbnail or kwargs.get('raw'):
        return

    if instance.image:
        instance.caption = instance.caption or instance.image.name
        instance.kind = 10
        instance.thumbnail = instance.image.url
        instance.code = '<img src="%s" alt="%s" />' % (
            instance.image.url, instance.caption)

    if "imgur" in instance.source:
        old_code = instance.source
        split = parse.urlsplit(instance.source)
        img_id = split.path[1:]  # sacamos el primer /
        if any(x in split.path for x in ('.gif', '.jpg', '.png',)):
            # es una imágen directa, sacamos la extensión
            img_id = img_id[:-4]

        instance.kind = 10
        instance.caption = old_code
        instance.thumbnail = "http://i.imgur.com/%st.jpg" % img_id
        instance.code = '<img src="http://i.imgur.com/%s.jpg" alt="%s" />' % (
            img_id, instance.caption)

    if "vimeo" in instance.source:
        options = {
            "url": instance.source,
            "&portrait": 0,
            "title": 0,
            "byline": 0,
        }
        target = "http://vimeo.com/api/oembed.json?%s" % parse.urlencode(
            options
        )
        response = requests.get(target)
        data = json.loads(response.text)

        instance.kind = 20
        instance.caption = data['title']
        instance.thumbnail = data['thumbnail_url']
        instance.code = data['html']

    instance.save()
