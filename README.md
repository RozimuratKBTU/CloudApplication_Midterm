# ☁️ Flask Meeting App — Scalable Web App on Google Cloud Platform

## 📘 Project Overview
This project demonstrates a **scalable Flask web application** deployed using multiple **Google Cloud Platform (GCP)** services.  
The goal is to create a **responsive, serverless, and containerized** application that is easy to maintain and can handle high traffic.

---

## 🧰 Key Technologies Used
- Google Cloud Platform (GCP)
- Google App Engine
- Google Cloud Functions
- Google Cloud Endpoints
- Google Kubernetes Engine (GKE)
- Docker
- Flask (Python)

---

## ⚙️ Project Structure
flaskProject/
│
├── main.py # Flask backend application
├── templates/ # HTML templates (index.html, create.html)
├── app.yaml # GCP App Engine configuration
├── openapi.yaml # Cloud Endpoints API definition
├── Dockerfile # Containerization setup
├── deployment.yaml # Kubernetes deployment configuration
├── service.yaml # Kubernetes service configuration
├── requirements.txt # Python dependencies
└── tests/ # Pytest-based test files


---

## 🚀 Deployment Steps

### 1️⃣ Deploy Flask App to App Engine
```bash

gcloud app deploy app.yaml


def greet_user(request):
    request_json = request.get_json(silent=True)
    if request_json and 'name' in request_json:
        name = request_json['name']
        return {'message': f'Hello, {name}! Welcome to EasyMeet!'}
    else:
        return {'error': 'No name provided'}, 400


Deploy the function with:

gcloud functions deploy greet_user \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated
