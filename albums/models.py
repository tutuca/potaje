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
    def first_image(self):
        return self.picture_set.all()[0].image

    @models.permalink
    def get_absolute_url(self):
        return ('album', (self.pk, ), )

    def __unicode__(self):
        return self.name


class Picture(models.Model):
    image = models.ImageField(upload_to='pictures')
    caption = models.CharField(max_length=128, null=True, blank=True)
    album = models.ForeignKey('Album')
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.image.name
