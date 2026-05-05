# Capstone Project: A Dying Planet

## Overview
This project explores how climate change is worsening globally over time. Using a dataset from Kaggle, we analyze how different countries are affected by climate trends and visualize these changes through an interactive dashboard.

## Project Structure
- **Backend (Thailand Griffith)**  
  FastAPI + SQLite  
  - Handles data storage and API endpoints  
  - Loads and processes climate data  
  - Provides secure access via API key authentication  

- **Frontend (Charles Simpson)**  
  Streamlit Dashboard  
  - Displays interactive visualizations  
  - Allows filtering by country, time, and climate element  
  - Communicates with backend through API requests  

## Technologies Used
- FastAPI
- SQLite
- Streamlit
- Pandas
- Pytest
- Flake8
- Google Cloud Storage (optional integration)

## Features
- REST API for climate data
- Interactive dashboard with filters
- Authentication (username/password + API key)
- Multiple data visualizations:
  - Climate trends over time
  - Top affected countries
  - Monthly climate patterns
- Clean, PEP8-compliant code
- Unit testing with pytest

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt

# 2. Running the FastAPI Application
# NOTE: The following code is for the first terminal.

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.backend.main:app --reload

# 3. Running the Streamlit Dashboard
# NOTE: The following code is for the second terminal.
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd src
cd frontend
streamlit run dashboard.py

# 4. CI/CD Testing and Code Quality Steps.
# NOTE: The following code is for the third terminal.
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
flake8 /workspaces/Capstone_Project_Charles-Simpson_Thailand-Griffith

# 5: API Endpoints and Documentation
# NOTE: The following code goes within the api.md Markdown.
## GET /data
Returns all climate data.

## POST /data
Adds new climate data.

## DELETE /data
Deletes climate data.
