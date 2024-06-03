from rest_framework.test import APITestCase
from unittest.mock import patch


class MeasurementViewSetTest(APITestCase):
    @patch("measurements.producer.ProducerMeasurement.publish")
    def test_create_measurement(self, mock_publish):
        data = {
            "system_id": 1,
            "timestamp": "2024-06-01T12:00:00Z",
            "ph": 7.0,
            "water_temperature": 25.0,
            "tds": 300.0,
        }
        response = self.client.post(
            "/api/v1/measurement/", data, format="json"
        )
        self.assertEqual(response.status_code, 201)
        mock_publish.assert_called_once()
