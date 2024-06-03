import django_filters
from .models import System


class SystemFilter(django_filters.FilterSet):
    setup_date = django_filters.DateFromToRangeFilter()
    capacity = django_filters.NumericRangeFilter()

    class Meta:
        model = System
        fields = ["setup_date", "capacity", "system_type", "is_active"]
