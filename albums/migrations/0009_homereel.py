# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0008_auto_20170611_2315"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeReel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reel", models.TextField(blank=True, editable=False, null=True)),
                ("reel_url", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
