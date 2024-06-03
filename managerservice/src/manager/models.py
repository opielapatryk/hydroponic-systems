from django.db import models


class System(models.Model):
    SYSTEM_TYPES = [
        ("NFT", "Nutrient Film Technique"),
        ("DWC", "Deep Water Culture"),
        ("EBB", "Ebb and Flow"),
        ("DRIP", "Drip System"),
        ("AERO", "Aeroponics"),
    ]

    name = models.CharField(max_length=100, unique=True)
    system_type = models.CharField(max_length=4, choices=SYSTEM_TYPES)
    capacity = models.FloatField(help_text="Capacity in liters", db_index=True)
    setup_date = models.DateField(auto_now_add=True, db_index=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    owner_id = models.IntegerField(db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["setup_date", "capacity"]),
        ]


class Measurement(models.Model):
    system = models.ForeignKey(
        System,
        related_name="measurements",
        on_delete=models.CASCADE,
        db_index=True,
    )
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    ph = models.FloatField()
    water_temperature = models.FloatField()
    tds = models.FloatField(help_text="Total Dissolved Solids")
