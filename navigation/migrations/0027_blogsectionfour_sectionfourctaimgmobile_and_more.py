# Generated by Django 4.2.1 on 2023-07-07 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0026_alter_userdata_page"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogsectionfour",
            name="sectionfourctaimgmobile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sectionfourctaimgmobile",
                to="navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="blogsectionthree",
            name="sectionthreeimgmobile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blogsectionthreeimgmobile",
                to="navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="blogsectiontwo",
            name="sectiontwoimg",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blogsectiontwoimg",
                to="navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="blogsectiontwo",
            name="sectiontwoimgmobile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blogsectiontwoimgmobile",
                to="navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="ourworksectionone",
            name="sectiononecolourtext",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ourworksectiontwo",
            name="sectiontwoimgmobile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ourworksectiontwoimgmobile",
                to="navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="blogicon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blogiconimage",
                to="navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="blogimage",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blogimage",
                to="navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="pageicon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pageicon",
                to="navigation.mediabucket",
            ),
        ),
        migrations.AddField(
            model_name="servicescta",
            name="Servicesctadiscription",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="page",
            name="pageimg",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pageimage",
                to="navigation.mediabucket",
            ),
        ),
    ]
