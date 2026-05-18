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

```bash
git clone https://github.com/vathsalasivapalan/networksecurity
cd networksecurity
pip install -r requirements.txt
python main.py
uvicorn app:app --reload
```

## Pipeline

MongoDB → Data Ingestion → Validation → Transformation → Model Training → MLflow → FastAPI

## Model performance
| Metric | Score |
|--------|-------|
| Accuracy | XX% |
| F1 Score | X.XX |
| Precision | X.XX |
| Recall | X.XX |

## Skills demonstrated
- End-to-end MLOps pipeline
- Experiment tracking with MLflow
- FastAPI REST endpoint
- MongoDB data ingestion
- Docker + GitHub Actions CI/CD