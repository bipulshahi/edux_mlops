import pathlib

import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from prediction_model.config import config
import numpy as np

#Numerical imputation - mean
class MeanImputer:
    def __init__(self):
        pass

    def fit(self):
        pass

    def transform(self):
        pass


#Categorical imputation - mode
class ModeImputer:
    def __init__(self):
        pass

    def fit(self):
        pass

    def transform(self):
        pass


#Drop columns
class DropColumns:
    def __init__(self):
        pass

    def fit(self):
        pass

    def transform(self):
        pass


#Domain Preprocessing
class DomainProcessing:
    def __init__(self):
        pass

    def fit(self):
        pass

    def transform(self):
        pass


#Custom label encoder
class CustomLabelEncoder:
    def __init__(self):
        pass

    def fit(self):
        pass

    def transform(self):
        pass



#Log transformation
class LogTransform:
    def __init__(self):
        pass

    def fit(self):
        pass

    def transform(self):
        pass