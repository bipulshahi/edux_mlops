import pytest
import sys
import os

import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model import predict

@pytest.fixture                      #decorator to execute single_prediction automatically when test_prediction.py executes by pytest
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[7:8]

    try:
        result = predict.generate_predictions(single_row)
        print(f"Predicted Outcome - {result}")
        return result
    except Exception as err:
        print(f"Got exception - {err}")
        raise

def test_single_pred_not_null(single_prediction):
    print("testing if predicted result is not null...")
    assert single_prediction is not None
    print("Test Passed: Single prediction is not none")


def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get("Predictions") , str)



def test_single_pred_validate(single_prediction):
    assert single_prediction.get("Predictions") == 'N'