# Generated by Django 4.2.1 on 2023-05-29 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0004_homepage_details_page_homepagereview_page_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="blog",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Blogsservicepages",
                to="navigation.blogs",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="homepage",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Homepageservicepages",
                to="navigation.homepage",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="ourwork",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Ourworkservicepages",
                to="navigation.ourwork",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="pricing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Pricingservicepages",
                to="navigation.pricing",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="whyus",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="whyusservicepages",
                to="navigation.whyus",
            ),
        ),
    ]
