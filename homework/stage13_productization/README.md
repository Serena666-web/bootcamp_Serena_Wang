Predictive Modeling + Flask API 

Project overview and objectives
This project trains a simple predictive model on time-series data and serves it via a lightweight Flask API. .

Repository layout (suggested)
.
├─ notebooks/ Jupyter notebooks (EDA, training, evaluation)
├─ src/ reusable code (features, utils)
├─ app.py Flask app exposing /predict and /plot
├─ model/ Serialized model bundle (model.pkl)
├─ requirements.txt
└─ README.txt

How to rerun scripts/notebooks
Prerequisites:

pip available

Environment setup:

python -m venv .venv
source .venv/bin/activate (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
Inside the training notebook:
Create features (e.g., lag_1, lag_2) and ensure numeric dtypes.
Split by time (no shuffling).
Fit a model (e.g., LinearRegression) and evaluate (RMSE/MAE).
Save a bundle to model/model.pkl containing:
model (fitted estimator)
features (list of feature names in the trained order)


Endpoints:

POST /predict
Request JSON: {"features":[...numbers...]}
Response JSON: {"prediction": <number>}

GET /predict/<x1>
Quick numeric test endpoint.

GET /predict/<x1>/<x2>
Quick numeric test endpoint (two inputs).

GET /plot