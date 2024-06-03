import json
import pika
import threading
from manager.models import Measurement

ROUTING_KEY = "measurements"
EXCHANGE = "measurements"
THREADS = 5
QUEUE = "measurements"


class MeasurementsListener(threading.Thread):
    """A class to consume messages from RabbitMQ and save measurements.

    This class extends threading.Thread to run as a separate thread. It consumes
    messages from RabbitMQ, parses them as JSON, and creates Measurement objects
    using the data from the messages.

    Attributes:
        ROUTING_KEY (str): The routing key for consuming messages.
        EXCHANGE (str): The name of the exchange.
        THREADS (int): The number of threads for consuming messages.
        QUEUE (str): The name of the queue.
    """

    ROUTING_KEY = "measurements"
    EXCHANGE = "measurements"
    THREADS = 5
    QUEUE = "measurements"

    def __init__(self):
        """Initialize the MeasurementsListener instance and set up the connection to RabbitMQ."""
        threading.Thread.__init__(self)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        self.channel = self.connection.channel()
        self.channel.exchange_declare(
            exchange=self.EXCHANGE, exchange_type="direct", durable=True
        )
        self.channel.queue_declare(queue=self.QUEUE, durable=True)
        self.channel.queue_bind(
            queue=self.QUEUE,
            exchange=self.EXCHANGE,
            routing_key=self.ROUTING_KEY,
        )
        self.channel.basic_qos(prefetch_count=self.THREADS * 10)
        self.channel.basic_consume(
            queue=self.QUEUE, on_message_callback=self.callback
        )

    def callback(self, channel, method, properties, body):
        """Process the received message and create Measurement objects.

        Args:
            channel: The channel object used for message processing.
            method: The method object containing message delivery information.
            properties: The properties of the received message.
            body (bytes): The body of the received message.

        Returns:
            None
        """
        try:
            data = json.loads(body)
            Measurement.objects.create(
                id=data["id"],
                system_id=data["system_id"],
                timestamp=data["timestamp"],
                ph=data["ph"],
                water_temperature=data["water_temperature"],
                tds=data["tds"],
            )
            channel.basic_ack(delivery_tag=method.delivery_tag)
        except (ValueError, KeyError) as e:
            print("Error processing message:", e)
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

    def run(self):
        """Start consuming messages from RabbitMQ."""
        print("Inside ManagerService: Created Listener")
        self.channel.start_consuming()
