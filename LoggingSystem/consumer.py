from kafka import KafkaConsumer
import json


def set_full_name(d):
    d["full_name"] = d['first_name']+d['last_name']
    return d


bootstrap_servers = ['localhost:9092']
topicName = 'new_topic123'
consumer = KafkaConsumer(topicName, group_id='group0', bootstrap_servers=bootstrap_servers, auto_offset_reset="earliest")
for msg in consumer:
    data = json.loads(msg.value)
    print(data)
    final_data = set_full_name(data)
    print(final_data)
    consumer.commit()

