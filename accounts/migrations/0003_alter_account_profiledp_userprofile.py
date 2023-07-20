# Generated by Django 4.2.1 on 2023-07-20 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0031_alter_blogauthor_profilephoto_and_more"),
        ("accounts", "0002_account_profiledp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="profiledp",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="profiledpjbkjb",
                to="navigation.mediabucket",
            ),
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("name", models.CharField(max_length=800)),
                (
                    "profiledp",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="profiledp",
                        to="navigation.mediabucket",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
        ),
    ]