import os
import pathlib
import pandas as pd
import joblib

import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from prediction_model.config import config

#loading the data
def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH,file_name)
    #print(filepath)
    _data = pd.read_csv(filepath)
    return _data

#save the model
def save_pipeline(model_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    joblib.dump(model_to_save, save_path)
    print(f"Model has been saved with the name {config.MODEL_NAME}")

#load the model
def load_pipeline(model_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH,model_to_load)
    model_loaded = joblib.load(save_path)
    print("Model has been loaded")
    return model_loaded


