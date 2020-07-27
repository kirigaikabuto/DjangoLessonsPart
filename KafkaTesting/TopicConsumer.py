# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
import json

import sys


bootstrap_servers = ['localhost:9092']


topicName = 'new_topic'


consumer = KafkaConsumer(topicName, group_id ='group4', bootstrap_servers =bootstrap_servers)


for msg in consumer:
    data = json.loads(msg.value)
    print(data['name'])


sys.exit()