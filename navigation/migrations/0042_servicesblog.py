# Generated by Django 4.2.1 on 2023-07-24 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0041_commonbranding"),
    ]

    operations = [
        migrations.CreateModel(
            name="Servicesblog",
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
                ("sectiontwoheading", models.TextField(blank=True, null=True)),
                (
                    "blogs",
                    models.ManyToManyField(
                        blank=True,
                        related_name="Servicesblogall",
                        to="navigation.blogpost",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Servicesblog",
                        to="navigation.page",
                    ),
                ),
            ],
        ),
    ]
