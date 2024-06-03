from django.core.management.base import BaseCommand
from broker.queue_listener import MeasurementsListener


class Command(BaseCommand):
    """Custom Django management command to launch RabbitMQ listener for measurement messages."""

    help = "Launches Listener for measurement message : RabbitMQ"

    def handle(self, *args, **options):
        """Handle method to start the RabbitMQ listener thread."""
        td = MeasurementsListener()
        td.start()
        self.stdout.write("Started Consumer Thread")
