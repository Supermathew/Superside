# Generated by Django 4.2.1 on 2023-05-29 02:34

import autoslug.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag", models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="Position",
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="name",
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="profilephoto",
        ),
        migrations.CreateModel(
            name="Ourworkproject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=800, unique=True)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="title", unique=True
                    ),
                ),
                ("projectsummary", models.TextField()),
                ("year", models.IntegerField()),
                ("industry", models.TextField()),
                ("body", ckeditor_uploader.fields.RichTextUploadingField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="servicesourwork",
                        to="navigation.page",
                    ),
                ),
                (
                    "projectthumbnail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projectthumbnailourwork",
                        to="navigation.mediabucket",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Blogauthor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bio", models.TextField()),
                ("Position", models.TextField()),
                ("name", models.CharField(max_length=225)),
                (
                    "profilephoto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profilephoto",
                        to="navigation.mediabucket",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="blogpost",
            name="Postauthor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blogpostauthor",
                to="navigation.blogauthor",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="navigation.tag"
            ),
        ),
    ]
