from django.db import models
import mistune

markdown = mistune.Markdown()


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    biopic = models.TextField()
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    rendered = models.TextField(editable=False)

    def __str__(self):
        return '%s Profile' % self.user.get_full_name()

    def save(self):
        self.rendered = markdown(self.biopic)


class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='services')
    endpoint = models.URLField(max_length=200)
    config = models.ManyToManyField(
        'auth.User',
        through='ServiceConfiguration'
    )

    def __str__(self):
        return self.name


class ServiceConfiguration(models.Model):
    profile = models.ForeignKey('auth.User')
    service = models.ForeignKey(Service)
    app_key = models.CharField(max_length=255, null=True, blank=True)
    app_secret = models.CharField(max_length=255, null=True, blank=True)
    user_profile = models.URLField(max_length=200)
