import pathlib
import os
import sys
import pandas as pd
import joblib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from packaging_ml_model.config import config

#print(config.DATAPATH)

#loading thr data
def load_dataset(file_name):
    file_path = os.path.join(config.DATAPATH,file_name)
    _data = pd.read_csv(file_path)
    return _data


#save the model
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print(f"Model has been saved with the name {config.MODEL_NAME}")


#load the model
def load_pipeline():
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    model_loaded = joblib.load(save_path)
    print("Model has been loaded")
    return model_loaded