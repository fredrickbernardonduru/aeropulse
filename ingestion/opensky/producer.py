import json
import logging
import signal
import time
from typing import Any

from kafka import KafkaProducer
from kafka.errors import KafkaError

from .client import OpenSkyClient
from .config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_CLIENT_ID,
    KAFKA_TOPIC,
    POLL_INTERVAL_SECONDS,
)
from .parser import parse_response


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    ),
)

logger = logging.getLogger(__name__)


class OpenSkyProducer:
    """
    Real-time OpenSky → Kafka ingestion service.
    """

    def __init__(self) -> None:
        self.running = True

        self.client = OpenSkyClient()

        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            client_id=KAFKA_CLIENT_ID,

            # Serialize Python dictionaries as JSON.
            value_serializer=lambda value: json.dumps(
                value
            ).encode("utf-8"),

            # Improve reliability.
            acks="all",

            # Retry transient Kafka failures.
            retries=5,

            # Ensure messages are sent in order for each
            # partition.
            max_in_flight_requests_per_connection=1,
        )

    def stop(self, signum: int | None = None, frame: Any = None) -> None:
        """
        Gracefully stop the producer.
        """

        logger.info("Shutdown signal received.")

        self.running = False

    def publish_record(
        self,
        record: dict[str, Any],
    ) -> None:
        """
        Publish one aircraft state to Kafka.
        """

        self.producer.send(
            KAFKA_TOPIC,
            value=record,
        )

    def ingest_once(self) -> int:
        """
        Perform one ingestion cycle.

        Returns
        -------
        int
            Number of records successfully submitted to Kafka.
        """

        logger.info(
            "Fetching latest aircraft states from OpenSky..."
        )

        response = self.client.get_states()

        records = parse_response(response)

        if not records:
            logger.warning(
                "OpenSky returned no aircraft states."
            )
            return 0

        published_count = 0

        for record in records:
            try:
                self.publish_record(record)
                published_count += 1

            except KafkaError:
                logger.exception(
                    "Failed to publish aircraft state."
                )

        # Wait for outstanding messages.
        self.producer.flush()

        logger.info(
            "Published %d aircraft states to Kafka topic '%s'.",
            published_count,
            KAFKA_TOPIC,
        )

        return published_count

    def run(self) -> None:
        """
        Continuously ingest OpenSky state vectors.
        """

        logger.info(
            "Starting AeroPulse OpenSky ingestion."
        )

        logger.info(
            "OpenSky endpoint: %s",
            self.client.session,
        )

        logger.info(
            "Kafka broker: %s",
            KAFKA_BOOTSTRAP_SERVERS,
        )

        logger.info(
            "Kafka topic: %s",
            KAFKA_TOPIC,
        )

        logger.info(
            "Polling interval: %s seconds",
            POLL_INTERVAL_SECONDS,
        )

        while self.running:

            cycle_start = time.monotonic()

            try:
                self.ingest_once()

            except Exception:
                logger.exception(
                    "Unexpected error during ingestion cycle."
                )

            elapsed = (
                time.monotonic() - cycle_start
            )

            sleep_time = max(
                0,
                POLL_INTERVAL_SECONDS - elapsed,
            )

            if self.running and sleep_time > 0:
                logger.info(
                    "Waiting %.2f seconds before next poll.",
                    sleep_time,
                )

                time.sleep(sleep_time)

        self.shutdown()

    def shutdown(self) -> None:
        """
        Gracefully close Kafka and HTTP connections.
        """

        logger.info(
            "Shutting down OpenSky producer..."
        )

        try:
            self.producer.flush()
            self.producer.close()
        finally:
            self.client.close()

        logger.info(
            "OpenSky producer stopped."
        )


def main() -> None:
    producer = OpenSkyProducer()

    signal.signal(
        signal.SIGINT,
        producer.stop,
    )

    signal.signal(
        signal.SIGTERM,
        producer.stop,
    )

    producer.run()


if __name__ == "__main__":
    main()