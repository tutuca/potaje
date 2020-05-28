# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0009_homereel"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="album", options={"ordering": ("-modified",)},
        ),
        migrations.AlterModelOptions(
            name="content",
            options={
                "verbose_name": "Contenido",
                "verbose_name_plural": "Contenido, fotos y videos.",
            },
        ),
        migrations.AlterModelOptions(
            name="homereel",
            options={
                "verbose_name": "Reel de la home",
                "verbose_name_plural": "Reeles de la home",
            },
        ),
        migrations.AlterModelOptions(
            name="section",
            options={
                "ordering": ("order",),
                "verbose_name": "Seccion",
                "verbose_name_plural": "Secciones",
            },
        ),
        migrations.AddField(
            model_name="album",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
