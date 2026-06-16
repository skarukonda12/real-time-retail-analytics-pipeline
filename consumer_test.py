from kafka import KafkaConsumer
import json
import psycopg2
conn=psycopg2.connect(host="localhost", database="retail_db",user="shivaprasadreddy")
cursor=conn.cursor()
consumer=KafkaConsumer(
    "retailer_detections",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset="earliest",
    group_id='retail_group'
)
print('waiting....')

for message in consumer:
     data=message.value
     label=data['label']
     conf=data['conf']
     img_path=data['img_path']

     cursor.execute(
             "INSERT INTO detections(label,confidence,img_path) VALUES (%s,%s,%s) ",
              (label,conf,img_path)
           )
     conn.commit()
     print("Inserted into PostgreSQL:", data)