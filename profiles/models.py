from django.db import models
import mistune


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    biopic = models.TextField()
    avatar = models.ImageField(upload_to="profiles", null=True, blank=True)
    rendered = models.TextField(editable=False)

    def __str__(self):
        return "%s Profile" % self.user.get_full_name()

    def save(self, *args, **kwargs):
        self.rendered = mistune.html(self.biopic)
        super().save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="services")
    endpoint = models.URLField(max_length=200)
    config = models.ManyToManyField("auth.User", through="ServiceConfiguration",)

    def __str__(self):
        return self.name


class ServiceConfiguration(models.Model):
    profile = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    service = models.ForeignKey("profiles.Service", on_delete=models.CASCADE)
    app_key = models.CharField(max_length=255, null=True, blank=True)
    app_secret = models.CharField(max_length=255, null=True, blank=True)
    user_profile = models.URLField(max_length=200)
