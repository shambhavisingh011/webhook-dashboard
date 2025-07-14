# 🚀 GitHub Webhook Dashboard

A Flask-based webhook receiver and UI dashboard that captures real-time **push** and **pull request** events from a GitHub repository using **webhooks**, stores them in **MongoDB**, and displays them in a clean, auto-refreshing UI.

---

## 📦 Features

- ✅ Receives GitHub Webhook events (`push` & `pull_request`)
- ✅ Stores event data in MongoDB
- ✅ Displays events in a responsive dashboard
- ✅ Polls every 15 seconds to show updates
- ✅ Supports testing via GitHub or curl
- ✅ Modular Flask structure for scalability

---

---

## ⚙️ Setup Instructions

### 🔹 1. Clone the repo

```bash
git clone https://github.com/shambhavisingh011/webhook-dashboard.git

cd webhook-dashboard

```
### 🔹 2  Create & activate a virtual environment
```bash
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```
### 🔹 3  Install dependencies
```bash
pip install -r requirements.txt
```

### 🔹 4  Start MongoDB
Ensure MongoDB is running locally at:
```bash
mongodb://localhost:27017
```
### 🔹 5  Run the Flask app
```bash
python run.py
```

Visit:
👉 http://localhost:5000

## 🌐 GitHub Webhook Setup

To test live events:

### 🔹 1  Start ngrok
```bash
ngrok http 5000
```
Copy the HTTPS URL (e.g. https://abc123.ngrok-free.app)

### 🔹 2 Add GitHub Webhook

In your GitHub repo (action-repo):

- Go to Settings 
-  Webhooks 
- Add Webhook

Payload URL:
```bash
https://abc123.ngrok-free.app/webhook
```
- Content type: application/json

- Events: ✅ Push, ✅ Pull request

- Click Add webhook

Now any push or PR triggers your dashboard!

## UI Output Format
Push Event:
```bash
📤 "Alice" pushed to "main" on 14th July 2025 - 7:30 PM UTC
```
Pull Request Event:
```bash
🔀 "Alice" submitted a pull request from "feature" to "main" on 14th July 2025 - 7:45 PM UTC
```

## 📌 Requirements

- Python 3.7+

- Flask

- Flask-PyMongo

- MongoDB

- Ngrok (for local testing)
