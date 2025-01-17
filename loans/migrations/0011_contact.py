# Generated by Django 5.0.7 on 2024-07-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loans", "0010_feedback"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("contact_no", models.CharField(max_length=15)),
                ("message", models.TextField()),
            ],
        ),
    ]
