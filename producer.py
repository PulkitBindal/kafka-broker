from confluent_kafka import Producer
import json
import time
# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
# Kafka producer function
def produce():
    producer = Producer(conf)
    # Produce some dummy data to Kafka topic
    for i in range(10):
        data = {
            'id': i,
            'name': f'name{i}',
            'value': i * 10
        }
        producer.produce('dummy-data', key=str(i), value=json.dumps(data))
        print(data)
        time.sleep(5)
    producer.flush()
# Kafka consumer function
produce()