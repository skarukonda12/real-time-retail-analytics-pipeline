import cv2
import numpy as np 
from ultralytics import YOLO
import psycopg2
import time
from kafka import KafkaProducer
import json

model=YOLO('yolov8n.pt')



cap =cv2.VideoCapture(0)
last_label=None
producer=KafkaProducer(
            bootstrap_servers="localhost:9092",
            value_serializer=lambda v:json.dumps(v).encode('utf-8')

 )
while True:
    ret, frame = cap.read()
    if not ret:
       break
    results=model(frame)
   
    
    
    for box in results[0].boxes:
       
       x1,y1,x2,y2=map(int,box.xyxy[0])
      
       cls=int(box.cls[0])
       label=results[0].names[cls]

       conf=float(box.conf[0])
      
       if conf < 0.60:
        continue
       print(label,conf)
       cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
       cv2.putText(frame,label,(x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2)
       filename=f"photos/{label}_{int(time.time())}.jpg"
       cv2.imwrite(filename,frame)
       

       if(last_label!=label):
         
         message={
            'label':label,
            'conf':conf,
            'img_path':filename
         }
         producer.send('retailer_detections',message)
         producer.flush()

        
         last_label=label
    if not cap.isOpened():
      print('camera is not opened')

    cv2.imshow('Camera', frame)

  
   
    if cv2.waitKey(1) == 27:
        break
    
cap.release() 
cv2.destroyAllWindows()



