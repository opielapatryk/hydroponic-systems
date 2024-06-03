import json
import pika

ROUTING_KEY = "measurements"
EXCHANGE = "measurements"
QUEUE = "measurements"
THREADS = 5


class ProducerMeasurement:
    """A class to produce and publish messages to RabbitMQ.

    This class provides methods to establish a connection to RabbitMQ,
    declare an exchange and a queue, bind the queue to the exchange,
    and publish messages to the exchange with the specified routing key.

    Attributes:
        ROUTING_KEY (str): The routing key for publishing messages.
        EXCHANGE (str): The name of the exchange.
        QUEUE (str): The name of the queue.
        THREADS (int): The number of threads for consuming messages.
    """

    ROUTING_KEY = "measurements"
    EXCHANGE = "measurements"
    QUEUE = "measurements"
    THREADS = 5

    def __init__(self) -> None:
        """Initialize the ProducerMeasurement instance and establish a connection to RabbitMQ."""
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()

        # Declare an exchange with the given name and type.
        self.channel.exchange_declare(
            exchange=self.EXCHANGE, exchange_type="direct", durable=True
        )

        # Declare a queue with the given name and durability.
        self.channel.queue_declare(queue=self.QUEUE, durable=True)

        # Bind the queue to the exchange with the routing key.
        self.channel.queue_bind(
            exchange=self.EXCHANGE,
            queue=self.QUEUE,
            routing_key=self.ROUTING_KEY,
        )

    def publish(self, message: dict):
        """Publish a message to RabbitMQ.

        Args:
            message (dict): The message to be published as a dictionary.

        Returns:
            None
        """
        # Publish a message to the exchange with the given routing key.
        self.channel.basic_publish(
            exchange=self.EXCHANGE,
            routing_key=self.ROUTING_KEY,
            body=json.dumps(
                message
            ),  # Convert the message dictionary to a JSON string.
            properties=pika.BasicProperties(
                delivery_mode=2,  # Make message persistent.
            ),
        )

    def close(self):
        """Close the connection to RabbitMQ."""
        # Close the connection to RabbitMQ.
        self.connection.close()
