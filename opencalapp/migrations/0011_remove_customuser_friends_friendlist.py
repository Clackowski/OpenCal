# Generated by Django 5.0.7 on 2024-08-27 04:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opencalapp", "0010_alter_calendar_contributors"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="friends",
        ),
        migrations.CreateModel(
            name="FriendList",
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
                (
                    "friends",
                    models.ManyToManyField(
                        blank=True, related_name="friends", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
