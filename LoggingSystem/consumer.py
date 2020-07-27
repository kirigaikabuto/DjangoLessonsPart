from kafka import KafkaConsumer
import json

bootstrap_servers = ['localhost:9092']
topicName = 'new_topic123'
consumer = KafkaConsumer(topicName, group_id='group3', bootstrap_servers=bootstrap_servers, auto_offset_reset="earliest")
for msg in consumer:
    data = json.loads(msg.value)
    print(data)
    consumer.commit()

