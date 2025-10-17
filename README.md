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
```


## 2️⃣ Deploy the function with:
```bash
gcloud functions deploy greet_user \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated
```

## 3️⃣ Containerize Application with Docker
```bash
docker build -t gcr.io/polar-ray-475006-i4/flask-meeting-app .
docker push gcr.io/polar-ray-475006-i4/flask-meeting-app
```

## 4️⃣ Deploy to Cloud Run (optional)
```bash
gcloud run deploy flask-meeting-app \
  --image gcr.io/polar-ray-475006-i4/flask-meeting-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## 5️⃣ Deploy to Kubernetes
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get service flask-meeting-service
```
Then open your app using the EXTERNAL-IP in your browser.

📊 Monitoring & Alerts

Integrated with Google Cloud Monitoring
Tracks metrics such as:
Request count
Error count
CPU & memory usage
Alerts configured to notify when errors exceed threshold.

## 🧪 Testing
Run tests locally using pytest:
```bash
pytest
```
## 🧠 Learning Outcomes

✅ Learned how to use multiple GCP services together
✅ Built and containerized a Flask app
✅ Deployed on App Engine, Cloud Run, and Kubernetes
✅ Integrated API with Cloud Endpoints and Cloud Functions
✅ Implemented monitoring and alerting
