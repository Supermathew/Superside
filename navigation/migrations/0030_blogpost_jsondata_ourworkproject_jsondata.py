# Generated by Django 4.2.1 on 2023-07-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0029_whyusmeta_servicesmeta_pricingmeta_ourworkmeta_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="jsondata",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ourworkproject",
            name="jsondata",
            field=models.TextField(blank=True, null=True),
        ),
    ]
