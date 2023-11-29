from sktime.forecasting.fbprophet import Prophet
from sktime.forecasting.base import ForecastingHorizon
from sklearn.metrics import mean_absolute_error as mae
import pickle
import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("test_ts_model")

with mlflow.start_run():
    y_test = pd.read_csv('/home/airflow/project/datasets/y_test.csv', index_col = 'Date', parse_dates = True)

    with open('/home/airflow/project/models/ProphetForecaster.pickle', 'rb') as model_file:
        model = pickle.load(model_file)
        fh = ForecastingHorizon(y_test.index, is_relative=False)
        y_pred = model.predict(fh)
        score = mae(y_pred.values, y_test.values)
        mlflow.log_artifact(local_path='/home/airflow/project/scripts/test_model.py',artifact_path="test_Prophet_model")
        mlflow.log_metric("score", float(score))
        mlflow.end_run()
