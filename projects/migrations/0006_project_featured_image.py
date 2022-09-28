# Generated by Django 4.1.1 on 2022-09-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0005_alter_project_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True,
                default="default.jpg",
                null=True,
                upload_to="featured_images",
            ),
        ),
    ]
