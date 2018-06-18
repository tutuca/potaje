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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('source', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='pictures', null=True)),
                ('kind', models.SmallIntegerField(default=10, choices=[(10, 'Picture'), (20, 'Video')])),
                ('caption', models.CharField(blank=True, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.URLField(editable=False)),
                ('code', models.TextField(editable=False)),
                ('album', models.ForeignKey(to='albums.Album', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='picture',
            name='album',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
