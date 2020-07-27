# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
import json

import sys


bootstrap_servers = ['localhost:9092']


topicName = 'new_topic'


consumer = KafkaConsumer(topicName, group_id ='group1', bootstrap_servers =bootstrap_servers)


for msg in consumer:
    data = json.loads(msg.value)
    print(data['name'])
    # print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))


sys.exit()