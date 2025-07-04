# Generated by Django 5.2.2 on 2025-06-16 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SimulatedConversation",
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
                    "dietary_preference",
                    models.CharField(
                        choices=[
                            ("NONE", "None"),
                            ("VE", "Vegetarian"),
                            ("VG", "Vegan"),
                        ],
                        default="NONE",
                        max_length=20,
                    ),
                ),
                ("favorite_foods", models.JSONField(default=list)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
