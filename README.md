# ☕ Nishh Reservations

A DevOps project that simulates a restaurant application (`Nishh Café Restro`) with full automation using Docker, GitLab CI/CD, and container orchestration tools. This repository is designed to showcase modern DevOps practices, including containerization, CI/CD pipeline integration, and infrastructure automation.

A simple, containerized café table reservation system built with **Flask**, **PostgreSQL**, and deployed on **Kubernetes**. This project allows customers to reserve tables online via a modern frontend connected to a RESTful backend API..

API Endpoints:
GET /reservations – Get all reservations
POST /reservations – Submit a new reservation

---

## 🚀 Features

- 📋 Online table reservation form
- 🔧 Python Flask backend (REST API)
- 🐘 PostgreSQL for persistent storage
- 🐳 Dockerized frontend and backend
- ☸️ Kubernetes deployments
- 🧭 Rancher-based Kubernetes management dashboard
- 📡 CORS-enabled API for frontend integration
- 🧪 Easy local and cluster testing

---

## 🗂️ Project Structure

nishh-reservations/ ├── backend/ │ ├── app.py │ ├── Dockerfile │ ├── requirements.txt │ └── backend-deployment.yaml ├── frontend/ │ ├── index.html │ ├── reservation.html │ ├── Dockerfile │ └── frontend-deployment.yaml ├── postgres/ │ ├── postgres-deployment.yaml │ └── postgres-service.yaml |


---

## ⚙️ Tech Stack

| Layer        | Tech          |
|--------------|---------------|
| Frontend     | HTML/CSS + JS |
| Backend      | Flask (Python)|
| Database     | PostgreSQL    |
| DevOps       | Docker + K8s  |
| DevOps       | Rancher       |
| Monitoring   | Grafana + Prometheus|

---
📬 Contact
Made with ❤️ by Hearsch-DevOps
