# Generated by Django 5.1.4 on 2024-12-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Events",
            fields=[
                ("eventName", models.CharField(max_length=64)),
                ("sport", models.CharField(max_length=64)),
                ("location", models.CharField(max_length=128)),
                ("desc", models.TextField()),
                ("date", models.DateField()),
                ("eventID", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]