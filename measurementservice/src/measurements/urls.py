from rest_framework.routers import DefaultRouter

from .views import MeasurementViewSet


router = DefaultRouter()
router.register(
    "api/v1/measurement", MeasurementViewSet, basename="measurements"
)

urlpatterns = router.urls
