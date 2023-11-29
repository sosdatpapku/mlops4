import pandas as pd
import numpy as np
from sktime.forecasting.model_selection import temporal_train_test_split
 
df = pd.read_csv('/home/airflow/project/datasets/data_processed.csv', index_col = 'Date', parse_dates = True)

y = df.resample('M').mean()
 
TEST_SIZE = int(0.1*y.size)

y_train, y_test = temporal_train_test_split(y, test_size=TEST_SIZE)


y_train.to_csv('/home/airflow/project/datasets/y_train.csv')
y_test.to_csv('/home/airflow/project/datasets/y_test.csv')
