# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.URLField(editable=False)),
                ('code', models.TextField(editable=False)),
                ('album', models.ForeignKey(to='albums.Album')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('source', models.URLField()),
                ('content_ptr', models.OneToOneField(primary_key=True, to='albums.Content', auto_created=True, serialize=False)),
            ],
            options={
            },
            bases=('albums.content',),
        ),
        migrations.AddField(
            model_name='picture',
            name='content_ptr',
            field=models.OneToOneField(primary_key=True, default='', to='albums.Content', auto_created=True, serialize=False),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='picture',
            name='album',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='created',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='id',
        ),
    ]
