from django.core.management.base import BaseCommand
import random
from faker import Faker
from measurements.models import Measurement


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Generates and saves a specified number of fake Measurement entries to the database.

        Args:
            num_measurements (int): The number of fake measurements to generate.
        """
        fake = Faker()
        system_ids = range(1, 101)  # Assuming system IDs are between 1 and 100

        for _ in range(1000):
            Measurement.objects.create(
                system_id=random.choice(system_ids),
                timestamp=fake.date_time_between(
                    start_date="-1y", end_date="now"
                ),
                ph=random.uniform(5.5, 7.5),
                water_temperature=random.uniform(15.0, 25.0),
                tds=random.uniform(300.0, 2000.0),
            )
