# Generated by Django 5.1.4 on 2024-12-26 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("create", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="events",
            old_name="name",
            new_name="eventName",
        ),
    ]