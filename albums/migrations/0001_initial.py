# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        primary_key=True,
                        verbose_name="ID",
                        auto_created=True,
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                ("description", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Picture",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        primary_key=True,
                        verbose_name="ID",
                        auto_created=True,
                    ),
                ),
                ("image", models.ImageField(upload_to="pictures")),
                ("caption", models.CharField(max_length=128, blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "album",
                    models.ForeignKey(to="albums.Album", on_delete=models.CASCADE),
                ),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        primary_key=True,
                        verbose_name="ID",
                        auto_created=True,
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                ("description", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ("id",)},
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name="album",
            name="section",
            field=models.ForeignKey(to="albums.Section", on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
