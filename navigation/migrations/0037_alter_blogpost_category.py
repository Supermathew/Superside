# Generated by Django 4.2.1 on 2023-07-22 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0036_remove_blogpost_page_alter_blogpost_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categoryBlogPost",
                to="navigation.category",
            ),
        ),
    ]