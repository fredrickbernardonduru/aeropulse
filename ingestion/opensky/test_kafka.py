from kafka import KafkaProducer


KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "flight-positions"


def main():

    print("Connecting to Kafka...")

    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda value: value.encode("utf-8"),
    )

    print("Connected to Kafka!")

    message = "AeroPulse Kafka connection test"

    print(f"Sending message: {message}")

    future = producer.send(
        KAFKA_TOPIC,
        value=message,
    )

    # Wait for Kafka to acknowledge the message.
    metadata = future.get(timeout=10)

    print("\nMessage successfully published!")

    print(f"Topic: {metadata.topic}")
    print(f"Partition: {metadata.partition}")
    print(f"Offset: {metadata.offset}")

    producer.flush()
    producer.close()

    print("\nKafka test completed successfully.")


if __name__ == "__main__":
    main()