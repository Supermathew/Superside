# Generated by Django 4.2.1 on 2023-07-02 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0021_whyussectionfive_sectionfivetopheading_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="singlereview",
            name="page",
        ),
        migrations.DeleteModel(
            name="Whyussectionfour",
        ),
    ]