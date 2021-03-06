import json
import requests
import mistune
import posixpath
from urllib import parse

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.html import strip_tags


class HomeReel(models.Model):
    reel = models.TextField(blank=True, null=True, editable=False)
    reel_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Reel de la home"
        verbose_name_plural = "Reeles de la home"

    def __str__(self):
        return self.reel_url

    def save(self):
        if self.reel_url:
            data = fetch_vimeo(self.reel_url)
            self.reel = responsive_embed(data["html"])

        super().save()


class Section(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(default="", blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    order = models.IntegerField()
    rendered = models.TextField(editable=False)
    reel = models.TextField(blank=True, null=True, editable=False)
    reel_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Secciones"
        ordering = ("order",)

    def __str__(self):
        return self.name

    def save(self):
        self.rendered = mistune.html(self.description)

        if self.reel_url:
            data = fetch_vimeo(self.reel_url)
            self.reel = responsive_embed(data["html"])

        super().save()


class Album(models.Model):
    name = models.CharField(max_length=60)
    section = models.ForeignKey("Section", models.CASCADE)
    description = models.TextField(default="", blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    rendered = models.TextField(editable=False)

    class Meta:
        ordering = ("-modified",)

    @property
    def cover(self):
        content = self.content_set.first()
        if content:
            return content.thumbnail

    def get_absolute_url(self):
        return (
            "album",
            (self.pk,),
        )

    def __str__(self):
        return self.name

    def save(self):
        self.rendered = mistune.html(self.description)
        super().save()


class Content(models.Model):
    source = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="pictures", null=True, blank=True)
    kind = models.SmallIntegerField(
        choices=((10, "Picture"), (20, "Video"),), default=10
    )
    caption = models.CharField(max_length=128, default="", blank=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    thumbnail = models.URLField(editable=False, default="")
    code = models.TextField(editable=False, default="")
    rendered = models.TextField(editable=False)

    def __str__(self):
        return strip_tags(self.rendered)[:100]

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural = "Contenido, fotos y videos."

    def save(self):
        self.rendered = mistune.html(self.caption)
        super().save()


def extract_img_id(source):
    path = parse.urlparse(source).path
    img_id = path
    if any(x in path for x in (".gif", ".jpg", ".png", ".jpeg")):
        # es una imagen directa, sacamos la extensión
        img_id = posixpath.basename(path)
    return img_id


@receiver(post_save, sender=Content)
def fetch_image(sender, instance, **kwargs):
    img_template = '<img class="img-fluid" src="%s" alt="%s" />'
    if instance.code:
        return

    elif instance.image:
        instance.caption = instance.caption or instance.image.name
        instance.kind = 10
        instance.thumbnail = instance.image.url
        instance.code = img_template % (instance.image.url, instance.caption)

    elif "imgur" in instance.source:
        old_code = instance.source

        img_id = extract_img_id(old_code)
        instance.kind = 10
        instance.caption = old_code
        instance.thumbnail = "http://i.imgur.com/%st.jpg" % img_id
        instance.code = img_template % (
            f"https://i.imgur.com/{img_id}.jpg",
            instance.caption,
        )

    elif "vimeo" in instance.source:
        data = fetch_vimeo(instance.source)

        instance.kind = 20
        instance.caption = data["title"]
        instance.thumbnail = data["thumbnail_url"]
        instance.code = responsive_embed(data["html"])

    instance.save()


def fetch_vimeo(url):

    options = {
        "url": url,
        "portrait": 0,
        "title": 0,
        "byline": 0,
    }
    target = "http://vimeo.com/api/oembed.json?%s" % parse.urlencode(options)
    response = requests.get(target)
    data = json.loads(response.text)
    return data


def responsive_embed(html):
    html = html.replace("<iframe", '<iframe class="embed-responsive-item"')
    embed = '<div class="embed-responsive embed-responsive-4by3">%s</div>'
    return embed % html
