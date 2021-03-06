# Generated by Django 3.0.6 on 2020-05-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0011_content_rendered"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="content",
            name="caption",
            field=models.CharField(blank=True, default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="section",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
    ]
