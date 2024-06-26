from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import SystemSerializer
from .models import System
from .filters import SystemFilter


class SystemViewSet(ModelViewSet):
    """
    A viewset for viewing and editing system instances.
    """

    serializer_class = SystemSerializer
    queryset = System.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = SystemFilter
    ordering_fields = ["setup_date", "capacity", "name"]
    ordering = ["setup_date"]

    def get_queryset(self):
        """
        This view should return a list of all the systems
        for the currently authenticated user.
        """
        user = self.request.user
        return System.objects.filter(owner_id=user.id)
