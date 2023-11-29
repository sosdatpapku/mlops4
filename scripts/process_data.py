import pandas as pd
import numpy as np
import mlflow
from mlflow.tracking import MlflowClient
 
mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("process_time_series")
with mlflow.start_run():
    df = pd.read_csv('/home/airflow/project/datasets/data.csv',  index_col = 'Date', parse_dates = True)

    # Оставим из всех данных только столбец Close, поскольку в дальнейшем для построения прогноза мы будем использовать только эту цену.
    df = df[['Close']].copy()
    
    # Переименуем столбец в 'Data' для простоты
    df = df.rename(columns={'Close': 'Data'})
    
    df['Data'] = df['Data'].astype('float32')
    
    df.to_csv('/home/airflow/project/datasets/data_processed.csv')

    mlflow.log_artifact(local_path="/home/airflow/project/scripts/process_data.py",artifact_path="process_time_series code")
    mlflow.end_run()
