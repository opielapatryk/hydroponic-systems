from rest_framework.viewsets import ModelViewSet
from .serializers import MeasurementSerializer
from .models import Measurement


class MeasurementViewSet(ModelViewSet):
    """
    A viewset for viewing and editing measurement instances.
    """

    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()