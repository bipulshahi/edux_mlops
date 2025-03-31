import pandas as pd
import numpy as np

import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from prediction_model.config import config

from prediction_model.processing.data_handling import load_dataset,save_pipeline
import prediction_model.pipeline as pipe

def perform_training():
    train_data = load_dataset(config.TRAIN_FILE)
    train_x = train_data[config.FEATURES]
    train_y = train_data[config.TARGET]
    pipe.classification_pipeline.fit(train_x,train_y)
    save_pipeline(pipe.classification_pipeline)


if __name__ == '__main__':
    perform_training()