# Generated by Django 4.1.3 on 2022-12-14 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("city", models.CharField(blank=True, max_length=50, null=True)),
                ("country", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
