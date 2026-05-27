# Network Security — Phishing URL Detection (MLOps Pipeline)

An end-to-end MLOps pipeline that detects phishing URLs using machine learning. The project covers the full data science lifecycle — from data ingestion via MongoDB to model training, experiment tracking with MLflow, and serving predictions through a FastAPI REST endpoint.

## Project Overview

Phishing attacks are one of the most common cyber threats. This project builds a production-ready pipeline to automatically classify URLs as **phishing** or **legitimate** using machine learning, with full experiment tracking and an API for real-time predictions.

## Tech Stack

| Area | Tools |
|------|-------|
| Machine Learning | Scikit-learn, XGBoost, imbalanced-learn |
| Experiment Tracking | MLflow, DagsHub |
| API | FastAPI, Uvicorn |
| Database | MongoDB Atlas |
| Data Processing | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Deployment | Docker, GitHub Actions (CI/CD) |

## Pipeline Architecture
MongoDB Atlas → Data Ingestion → Data Validation → Data Transformation → Model Training → MLflow Tracking → FastAPI Endpoint

## Project Structure
networksecurity/
│
├── networksecurity/          # Core pipeline modules
│   ├── components/           # Ingestion, Validation, Transformation, Trainer
│   ├── entity/               # Config and artifact entities
│   ├── exception/            # Custom exception handling
│   └── logging/              # Pipeline logging
│
├── notebooks/                # EDA and experiments
├── Network_Data/             # Raw data
├── templates/                # FastAPI HTML templates
├── app.py                    # FastAPI application
├── main.py                   # Training pipeline entry point
├── push_data.py              # MongoDB data ingestion script
├── requirements.txt
├── Dockerfile
└── setup.py

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/vathsalasivapalan/networksecurity.git
cd networksecurity
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**

Create a `.env` file with your MongoDB connection string:
MONGO_DB_URL=your_mongodb_atlas_connection_string

**4. Push data to MongoDB**
```bash
python push_data.py
```

**5. Run the training pipeline**
```bash
python main.py
```

**6. Start the FastAPI server**
```bash
uvicorn app:app --reload
```

**7. Open the API docs**

Navigate to: `http://localhost:8000/docs`

## Skills Demonstrated

- End-to-end MLOps pipeline design and implementation
- Modular, production-style Python project structure
- MongoDB Atlas for cloud data storage and ingestion
- Experiment tracking and model registry with MLflow and DagsHub
- REST API development with FastAPI
- Docker containerisation
- CI/CD automation with GitHub Actions
- Handling class imbalance with imbalanced-learn

## Author

**Vathsala Sivapalan**  
[GitHub](https://github.com/vathsalasivapalan) 
