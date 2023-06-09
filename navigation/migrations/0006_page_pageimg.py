# Generated by Django 4.2.1 on 2023-05-30 01:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        (
            "navigation",
            "0005_page_blog_page_homepage_page_ourwork_page_pricing_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="pageimg",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pageimage",
                to="navigation.mediabucket",
            ),
            preserve_default=False,
        ),
    ]
