# Generated by Django 5.0.6 on 2024-06-03 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="System",
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
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "system_type",
                    models.CharField(
                        choices=[
                            ("NFT", "Nutrient Film Technique"),
                            ("DWC", "Deep Water Culture"),
                            ("EBB", "Ebb and Flow"),
                            ("DRIP", "Drip System"),
                            ("AERO", "Aeroponics"),
                        ],
                        max_length=4,
                    ),
                ),
                (
                    "capacity",
                    models.FloatField(db_index=True, help_text="Capacity in liters"),
                ),
                ("setup_date", models.DateField(auto_now_add=True, db_index=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("owner_id", models.IntegerField(db_index=True)),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["setup_date", "capacity"],
                        name="manager_sys_setup_d_dde881_idx",
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name="Measurement",
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
                ("timestamp", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("ph", models.FloatField()),
                ("water_temperature", models.FloatField()),
                ("tds", models.FloatField(help_text="Total Dissolved Solids")),
                (
                    "system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="measurements",
                        to="manager.system",
                    ),
                ),
            ],
        ),
    ]
