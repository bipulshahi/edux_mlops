import mlflow
import os
import argparse
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

mlflow.mlflow.set_tracking_uri("http://127.0.0.1:5000")

def load_data():
    URL = 'https://raw.githubusercontent.com/bipulshahi/Dataset/refs/heads/main/winequality-red.csv'
    try:
        df = pd.read_csv(URL, sep=';')
        return df
    except Exception as err:
        raise err

def eval_function(actual,pred):
    rmse = (mean_squared_error(actual,pred))**0.5
    mae = mean_absolute_error(actual,pred)
    r2 = r2_score(actual,pred)
    return rmse,mae,r2



def main(alpha,l1_ratio):
    df = load_data()
    TARGET = "quality"
    X = df.drop(columns=TARGET)
    y = df[TARGET]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

    mlflow.set_experiment("Wine_Quality_Exp")
    with mlflow.start_run():
        mlflow.log_param("Alpha" , alpha)
        mlflow.log_param("L1_Ratio" , l1_ratio)

        model = ElasticNet(alpha = alpha , l1_ratio = l1_ratio)
        model.fit(X_train,y_train)
        y_pred = model.predict(X_test)
        rmse,mae,r2 = eval_function(y_test,y_pred)
        mlflow.log_metric("RMSE" , rmse)
        mlflow.log_metric("MAE" , mae)
        mlflow.log_metric("R2_Score" ,r2)
        mlflow.sklearn.log_model(model,"trained_model")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--alpha','-a',type=float,default=0.2)
    args.add_argument('--l1_ratio','-l1',type=float,default=0.3)
    parsed_args = args.parse_args()
    main(parsed_args.alpha, parsed_args.l1_ratio)