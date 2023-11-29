import pandas as pd
import pickle
import mlflow
from mlflow.tracking import MlflowClient
from sktime.forecasting.fbprophet import Prophet
from sktime.forecasting.base import ForecastingHorizon

mlflow.set_tracking_uri("http://0.0.0.0:5000")
mlflow.set_experiment("train_ts_model")
with mlflow.start_run():

    y_train = pd.read_csv('/home/airflow/project/datasets/y_train.csv', index_col = 'Date', parse_dates = True)
    y_test = pd.read_csv('/home/airflow/project//datasets/y_test.csv', index_col = 'Date', parse_dates = True)

    fh = ForecastingHorizon(y_test.index, is_relative=False)

    forecaster = Prophet(add_seasonality = {'name':'season','period':5, 'fourier_order':13, 'mode':'additive'},
                    seasonality_mode='additive',
                    yearly_seasonality=True,
                    growth="linear",
                    holidays_prior_scale=0,
    changepoint_prior_scale=0.01,
    n_changepoints=5,
    weekly_seasonality=False,
    daily_seasonality=True,
    seasonality_prior_scale=1.0,
    holidays=None,
    changepoints=None,
    mcmc_samples=0)
    forecaster.fit(y_train)
    
    mlflow.log_artifact(local_path="/home/airflow/project/scripts/train_model.py",artifact_path="train_ts_model code")
    mlflow.end_run()
    # Save the model using pickle
    with open('/home/airflow/project/models/ProphetForecaster.pickle', 'wb') as model_file:
        pickle.dump(forecaster, model_file)
