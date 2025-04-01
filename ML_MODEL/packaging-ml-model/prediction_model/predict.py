import pandas as pd
import numpy as np
import joblib

import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from prediction_model.config import config

from prediction_model.processing.data_handling import load_dataset,load_pipeline

_model = load_pipeline(config.MODEL_NAME)

'''
def generate_predictions(data_input):
    data = pd.DataFrame(data_input, columns = config.FEATURES)
    pred = _model.predict(data)[0]
    result = {"Predictions" : pred}
    return result



print(generate_predictions([['Male','Yes','0','Graduate','No',5720,0,110,340,1,'Urban']]))
'''

def generate_predictions():
    test_data = load_dataset(config.TEST_FILE)
    pred = _model.predict(test_data[config.FEATURES])
    result = {"Predictions" : pred}
    print(result)
    return result

generate_predictions()