# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('caption', models.CharField(max_length=128, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('source', models.URLField()),
                ('thumbnail', models.URLField(editable=False)),
                ('html', models.TextField(editable=False)),
                ('album', models.ForeignKey(to='albums.Album')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
