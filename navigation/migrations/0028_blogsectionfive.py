# Generated by Django 4.2.1 on 2023-07-07 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0027_blogsectionfour_sectionfourctaimgmobile_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blogsectionfive",
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
                ("sectionfiveheading", models.TextField(blank=True, null=True)),
                ("sectionfivesubheading", models.TextField(blank=True, null=True)),
                ("sectionfivediscription", models.TextField(blank=True, null=True)),
                (
                    "sectionfiveemailplaceholder",
                    models.TextField(blank=True, null=True),
                ),
                ("sectionfivetext", models.TextField(blank=True, null=True)),
                ("sectionfivebtnurl", models.TextField(blank=True, null=True)),
                (
                    "page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Blogsectionfive",
                        to="navigation.blogs",
                    ),
                ),
            ],
        ),
    ]
