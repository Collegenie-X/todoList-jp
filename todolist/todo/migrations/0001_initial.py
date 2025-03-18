# Generated by Django 5.1.6 on 2025-03-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("is_done", models.BooleanField(default=False)),
                (
                    "priority",
                    models.IntegerField(
                        choices=[(1, "Low"), (2, "Normal"), (3, "High")], default=2
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
