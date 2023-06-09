# Generated by Django 4.2.1 on 2023-06-19 08:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_wishlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carousel",
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
                ("image", models.ImageField(upload_to="photos/carousel")),
                ("title", models.CharField(max_length=150)),
                ("sub_title", models.CharField(max_length=100)),
            ],
        ),
    ]
