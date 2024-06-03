from rest_framework.viewsets import ModelViewSet
from .serializers import MeasurementSerializer
from .models import Measurement
from .producer import ProducerMeasurement


class MeasurementViewSet(ModelViewSet):
    """
    A viewset for viewing and editing measurement instances.
    """

    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()

    def __init__(self, *args, **kwargs):
        """
        Initialize the viewset and the RabbitMQ producer.
        """
        super().__init__(*args, **kwargs)
        self.producer = ProducerMeasurement()

    def perform_create(self, serializer):
        """
        Save a new measurement instance and send a message to RabbitMQ.

        This method saves a new measurement instance using the provided serializer,
        then sends a message containing the measurement details to RabbitMQ.
        """
        instance = serializer.save()
        message = {
            "id": instance.id,
            "system_id": instance.system_id,
            "timestamp": instance.timestamp.isoformat(),  # Convert datetime to ISO format string
            "ph": instance.ph,
            "water_temperature": instance.water_temperature,
            "tds": instance.tds,
        }
        self.producer.publish(message)
