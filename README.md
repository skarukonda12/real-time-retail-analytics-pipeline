# Real-Time Object Detection Analytics Pipeline

## Overview

A production-style real-time object detection and analytics pipeline built using YOLOv8, Apache Kafka, PostgreSQL, Docker, and Streamlit.
The system captures live video from a webcam, detects objects using * YOLOv8 *, streams detection events through *Kafka*, stores them in *PostgreSQL*, and visualizes analytics through an interactive *Streamlit* dashboard

# Architecture
flowchart TD
    A[Webcam] --> B[YOLOv8 Object Detection]
    B --> C[Kafka Producer]
    C --> D[Apache Kafka Topic]
    D --> E[Kafka Consumer]
    E --> F[PostgreSQL Database]
    F --> G[Streamlit Dashboard]
## Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Programming |
| YOLOv8 | Real-Time Object Detection |
| OpenCV | Video Processing |
| Apache Kafka | Event Streaming |
| PostgreSQL | Data Storage |
| Streamlit | Dashboard & Analytics |
| Docker | Kafka Containerization |
| Pandas | Data Analysis |
| NumPy | Numerical Processing |

## Features
### Real-Time Object Detection
Detects objects from live webcam feed
Displays bounding boxes and labels
Captures confidence scores

### Kafka Streaming
Producer sends object detection events
Kafka topic acts as message broker
Consumer independently processes events

### PostgreSQL Storage
Stores:

Object Label
Confidence Score
Image Path
Detection Timestamp

### Interactive Dashboard
 View all detections
 Filter by object type
 Filter by date
 Search detections
 Download CSV reports
 View recent detection images
 Visualize object frequency

### Project Structure
- video_object_detection.py — YOLO object detection from webcam
- producer_test.py — Kafka producer for sending detection events
- consumer_test.py — Kafka consumer for processing events and storing in PostgreSQL
- dashboard.py — Streamlit dashboard for analytics and visualization
- docker-compose.yaml — Docker configuration for Apache Kafka
- requirements.txt — Python dependencies
- .gitignore — Files and folders excluded from Git tracking
- README.md — Project documentation
- photos/ — Stores captured object detection images
### Database Schema
CREATE TABLE detections (
    id SERIAL PRIMARY KEY,
    label VARCHAR(100),
    confidence FLOAT,
    img_path TEXT,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
### Sample Kafka Message
{
  "label": "bottle",
  "conf": 0.87,
  "img_path": "photos/bottle_123456.jpg"
}
## Installation
### Clone Repository
 git clone https://github.com/skarukonda12/real-time-retail-analytics-pipeline.git
 cd real-time-retail-analytics-pipeline
### Install Dependencies
 pip install -r requirements.txt
### Start Kafka Using Docker
 docker compose up -d
 Verify:
 docker ps
## Running the Project
### Start Kafka Consumer
 python consumer_test.py
### Start YOLO Detection Producer
 python video_object_detection.py
### Launch Dashboard
 streamlit run dashboard.py
## Key Concepts Demonstrated
 Real-Time Data Streaming
 Event-Driven Architecture
 Kafka Producer & Consumer
 PostgreSQL Integration
 Computer Vision with YOLOv8
 Docker Fundamentals
 Streamlit Dashboard Development
 Data Engineering Pipeline Design
## Future Enhancements
 Multi-Camera Support
 Object Tracking
 Cloud Deployment (AWS/Azure/GCP)
 Apache Airflow Orchestration
 Dockerized PostgreSQL
 Kafka Partition Scaling
 Real-Time Alerting System
## Resume Highlights
 Built a real-time retail analytics pipeline using YOLOv8, Apache Kafka, PostgreSQL, Docker, and Streamlit.
 Designed an event-driven architecture to stream object detection events through Kafka.
 Developed a PostgreSQL-backed analytics dashboard with filtering, search, visualization, and CSV export capabilities.
 Implemented real-time computer vision workflows and message-driven data processing.
