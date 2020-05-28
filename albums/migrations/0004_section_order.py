# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0003_auto_20150215_1811"),
    ]

    operations = [
        migrations.AddField(
            model_name="section",
            name="order",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
