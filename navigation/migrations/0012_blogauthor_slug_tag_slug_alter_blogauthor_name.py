# Generated by Django 4.2.1 on 2023-06-01 15:08

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0011_emailinput_social"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogauthor",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=django.utils.timezone.now,
                editable=False,
                populate_from="name",
                unique=True,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tag",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=django.utils.timezone.now,
                editable=False,
                populate_from="name",
                unique=True,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="blogauthor",
            name="name",
            field=models.CharField(max_length=225, unique=True),
        ),
    ]
