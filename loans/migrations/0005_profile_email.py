# Generated by Django 5.0.7 on 2024-07-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loans", "0004_alter_profile_uid"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.CharField(default="", max_length=20),
            preserve_default=False,
        ),
    ]