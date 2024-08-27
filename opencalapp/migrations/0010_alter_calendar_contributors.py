# Generated by Django 5.0.7 on 2024-08-15 03:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opencalapp", "0009_customuser_friends_alter_calendar_contributors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendar",
            name="contributors",
            field=models.ManyToManyField(
                blank=True, related_name="active_calendars", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]