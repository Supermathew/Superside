# Generated by Django 4.2.1 on 2023-07-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "navigation",
            "0020_rename_sectionfiveparagraph_whyussectionfive_sectionfivecolourtext_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="whyussectionfive",
            name="sectionfivetopheading",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="whyussectionfive",
            name="sectionfivetopsubheading",
            field=models.TextField(blank=True, null=True),
        ),
    ]
