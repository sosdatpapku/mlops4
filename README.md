# mlops4
Проект в рамках ДЗ№4 по MLOps
Цель эксперимента: Автоматизация оценки качества модели прогнозирования временных рядов при изменении набора гиперпараметров по целевой метрике (Mean Absolute Error)

Инструменты:  
Oracle VM VirtualBox - для развертывания виртуальной машины  
Linux Ubuntu 22.04.03 - в качестве ОС  
Python 3.10.12 - в качестве ЯП для написания скриптов  
Prophet - в качестве модели прогнозирования ВР  
Airflow - в качестве ETL-инструмента  
MLFlow - для логирования экспериментов и артефактов (в нашем случае метрики предсказания)  

Датасет: данные по стоимости акций компании Nike из датасета "[DJIA 30 Stock Time Series](https://www.kaggle.com/datasets/szrlee/stock-time-series-20050101-to-20171231)"  

Структура работы DAG-файла stock_forecast в Airflow  (см.скрин ниже)  
![image](https://github.com/sosdatpapku/mlops4/assets/114177169/4b1425a2-f658-456e-b5a3-e8999b8c67d2)  

Отслеживание метрики MAE на графике в MLFlow (см. скрин ниже)  
![image](https://github.com/sosdatpapku/mlops4/assets/114177169/2dc2a4b1-d0a4-4f8b-a0bf-36777b5d9ef7)

