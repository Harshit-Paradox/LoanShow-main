# Generated by Django 5.0.7 on 2024-07-20 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("loans", "0008_remove_profile_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="email",
        ),
    ]
