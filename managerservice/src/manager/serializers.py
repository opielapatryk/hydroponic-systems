from rest_framework import serializers
from .models import System, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["timestamp", "ph", "water_temperature", "tds"]


class SystemSerializer(serializers.ModelSerializer):
    measurements = serializers.SerializerMethodField()

    class Meta:
        model = System
        fields = [
            "id",
            "name",
            "system_type",
            "capacity",
            "setup_date",
            "location",
            "is_active",
            "owner_id",
            "measurements",
        ]

    def get_measurements(self, obj):
        measurements = obj.measurements.order_by("-timestamp")[:10]
        return MeasurementSerializer(measurements, many=True).data
