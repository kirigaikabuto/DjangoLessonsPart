# Import KafkaProducer from Kafka library
from kafka import KafkaProducer
import json
# Define server with port
bootstrap_servers = ['localhost:9092']

d = {
    "name":"yerassyl"
}

# Define topic name where the message will publish
topicName = 'new_topic'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

data_json = json.dumps(d)
# Publish text in defined topic


#перевести строку в байты при помощи функции
producer.send(topicName,bytearray(data_json, 'utf-8'))


producer.flush()