# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_auto_20170609_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
    ]