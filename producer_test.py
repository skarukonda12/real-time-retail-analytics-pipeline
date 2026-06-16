from kafka import KafkaProducer
import json

producer=KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v:json.dumps(v).encode('utf-8')

)

message={'label':'bottle',
         'conf':0.42,
         'img_path':'photos/bottle_test.jpg'}

producer.send('retailer_detections',message)
producer.flush()
print('message sent succesfully')

    

