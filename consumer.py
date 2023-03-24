from confluent_kafka import Consumer
import json

# Kafka consumer function
def consume():
    consumer_conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'python-consumer',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(consumer_conf)
    # Subscribe to Kafka topic
    consumer.subscribe(['dummy-data'])
    # Consume messages from Kafka topic
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f'Consumer error: {msg.error()}')
            continue
        # Process received message
        key = msg.key()
        value = json.loads(msg.value())
        print(f'Key: {key}, Value: {value}')
    consumer.close()

consume()