# Generated by Django 4.2.1 on 2023-06-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_rename_image_carousel_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carousel",
            name="sub_title",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="carousel",
            name="title",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
