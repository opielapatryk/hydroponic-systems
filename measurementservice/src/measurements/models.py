from django.db import models


class Measurement(models.Model):
    system_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ph = models.FloatField()
    water_temperature = models.FloatField()
    tds = models.FloatField(help_text="Total Dissolved Solids")

    def __str__(self):
        return f"{self.system_id, self.timestamp, self.ph, self.water_temperature, self.tds}"
