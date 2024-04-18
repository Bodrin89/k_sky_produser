import os
from json import dumps

from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

topic_name = 'send_checks'

bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda x: dumps(x).encode('utf-8'))


def send_messages(data):
    """Отправка сообщения в сервис приема чеков"""
    producer.send(topic_name, value=data)
