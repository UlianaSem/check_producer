import json
import logging

from confluent_kafka import Producer
from django.conf import settings


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

config = {
    'bootstrap.servers': f'{settings.KAFKA_HOST}:9092',
    'client.id': settings.KAFKA_CLIENT,
    'group.id': settings.KAFKA_CLIENT,
}

producer = Producer(config)


def serialize_data(data):
    for item in data['items']:
        item['price'] = float(item['price'])

    return json.dumps(data)


def send_message(topic, data):
    serialized_data = serialize_data(data)
    producer.produce(topic, value=serialized_data)

    logger.info(f'Sent check {data.get("transaction_id")}')
    producer.flush()
