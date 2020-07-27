from kafka import KafkaProducer
import json


def send_log(log):
    bootstrap_servers = ['localhost:9092']
    topic_name = 'new_topic123'
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    data_json = json.dumps(log)
    producer.send(topic_name, bytearray(data_json, 'utf-8'))
    producer.flush()
