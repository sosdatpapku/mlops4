import requests
import json
import os
import mlflow
from mlflow.tracking import MlflowClient
 
mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("get_timeseries_data")
with mlflow.start_run():
    df = requests.get("https://raw.githubusercontent.com/sosdatpapku/mlops4/main/datasets/NKE_2006-01-01_to_2018-01-01.csv")
    
    with open("/home/airflow/project/datasets/data.csv", "w") as f:
        f.write(df.text)
        mlflow.log_artifact(local_path="/home/airflow/project/scripts/get_data.py",artifact_path="get_ts_data code")
        mlflow.end_run()
