# Network Security — Phishing URL Detection

An end-to-end MLOps pipeline that detects phishing URLs using machine learning. Built with FastAPI, MLflow, MongoDB, Docker, and GitHub Actions CI/CD.

## What it does
Classifies URLs as phishing or legitimate using a trained ML model. Exposes predictions via a FastAPI endpoint and tracks all experiments with MLflow.

## Tech stack
| Area | Tools |
|------|-------|
| ML | Scikit-learn |
| Experiment tracking | MLflow |
| API | FastAPI |
| Database | MongoDB Atlas |
| Deployment | Docker, GitHub Actions |

## How to run
1. Clone the repo
2. Run: pip install -r requirements.txt
3. Run: python main.py
4. Run: uvicorn app:app --reload
5. Open: http://localhost:8000/docs

## Pipeline
MongoDB → Data Ingestion → Validation → Transformation → Model Training → MLflow → FastAPI

## Skills demonstrated
- End-to-end MLOps pipeline
- Experiment tracking with MLflow
- FastAPI REST endpoint
- MongoDB data ingestion
- Docker and GitHub Actions CI/CD