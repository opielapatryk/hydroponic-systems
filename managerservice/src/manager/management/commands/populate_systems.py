from django.core.management.base import BaseCommand
import random
from faker import Faker
from manager.models import System


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Populate the System model with fake data.

        This script creates 100 System objects with randomly generated attributes
        using the Faker library. The generated data includes unique company names,
        random system types, capacities, locations, and ownership assigned to
        random user IDs.

        Usage:
            Run this script to populate the System model with fake data:
                python populate_systems.py
        """
        fake = Faker()

        # Define possible system types
        SYSTEM_TYPES = ["NFT", "DWC", "EBB", "DRIP", "AERO"]

        # List of user IDs to assign ownership of systems
        user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Generate and create 100 System objects
        for _ in range(100):
            System.objects.create(
                name=fake.unique.company(),
                system_type=random.choice(SYSTEM_TYPES),
                capacity=random.uniform(50.0, 1000.0),
                location=fake.address(),
                is_active=random.choice([True, False]),
                owner_id=random.choice(user_ids),
            )
