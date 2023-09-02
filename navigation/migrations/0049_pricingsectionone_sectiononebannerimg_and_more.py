# Generated by Django 4.2.1 on 2023-09-01 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0048_alter_blogauthor_options_alter_blogpost_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pricingsectionone",
            name="sectiononebannerimg",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sectiononebannerimg",
                to="navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="pricingsectionone",
            name="sectiononecheckoutbtnlink",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pricingsectionone",
            name="sectiononecheckoutbtntext",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pricingsectionone",
            name="sectiononeplandisc",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pricingsectionone",
            name="sectiononeplantext",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pricingsectiontwo",
            name="sectiontwofeaturetext",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="Pricingsinglefaq",
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
                ("Pricingsinglefaqheading", models.TextField(blank=True, null=True)),
                ("Pricingsinglefaqsubheading", models.TextField(blank=True, null=True)),
                (
                    "Pricingsinglefaqimg",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Pricingsinglefaqimg",
                        to="navigation.mediabucket",
                    ),
                ),
                (
                    "Pricingsinglefaqmobileimg",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Pricingsinglefaqmobileimg",
                        to="navigation.mediabucket",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Pricingsinglefaq",
                        to="navigation.pricing",
                    ),
                ),
            ],
        ),
    ]
