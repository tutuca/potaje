# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='profiles', blank=True, null=True),
            preserve_default=True,
        ),
    ]
