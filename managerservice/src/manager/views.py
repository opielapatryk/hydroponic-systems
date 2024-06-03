from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import SystemSerializer
from .models import System


class SystemViewSet(ModelViewSet):
    """
    A viewset for viewing and editing system instances.
    """

    serializer_class = SystemSerializer
    queryset = System.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the systems
        for the currently authenticated user.
        """
        user = self.request.user
        return System.objects.filter(owner_id=user.id)
