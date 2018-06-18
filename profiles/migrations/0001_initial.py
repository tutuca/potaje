# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('biopic', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='services')),
                ('endpoint', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceConfiguration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('app_key', models.CharField(blank=True, max_length=255, null=True)),
                ('app_secret', models.CharField(blank=True, max_length=255, null=True)),
                ('user_profile', models.URLField()),
                ('profile', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='service',
            name='config',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='profiles.ServiceConfiguration'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serviceconfiguration',
            name='service',
            field=models.ForeignKey(to='profiles.Service', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
