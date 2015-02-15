# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_auto_20140709_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='code',
            field=models.TextField(editable=False, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='thumbnail',
            field=models.URLField(editable=False, default=''),
            preserve_default=True,
        ),
    ]
