import pathlib

import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from prediction_model.config import config
import numpy as np

#Numerical imputation - mean
class MeanImputer:
    def __init__(self,vars=None):
        self.variables = vars

    def fit(self,X,y=None):
        self.mean_dict = {}
        for var in self.variables:
            self.mean_dict[var] = X[var].mean()
        return self

    def transform(self,X):
        for var in self.variables:
            X[var] = X[var].fillna(self.mean_dict[var])
        return X


#Categorical imputation - mode
class ModeImputer:
    def __init__(self,vars=None):
        self.variables = vars

    def fit(self,X,y=None):
        self.mode_dict = {}
        for var in self.variables:
            self.mode_dict[var] = X[var].mode()[0]
        return self

    def transform(self,X):
        for var in self.variables:
            X[var] = X[var].fillna(self.mode_dict[var])
        return X


#Drop columns
class DropColumns:
    def __init__(self,vars_to_drop = None):
        self.variables_to_drop = vars_to_drop

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        X = X.drop(columns = [self.variables_to_drop])
        return X


#Domain Preprocessing
class DomainProcessing:
    def __init__(self,vars_to_modify=None,vars_to_add=None):
        self.variables_to_modify = vars_to_modify
        self.variables_to_add = vars_to_add

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        for feature in self.variables_to_modify:
            X[feature] = X[feature] + X[self.variables_to_add]
        return X


#Custom label encoder
class CustomLabelEncoder():
  def __init__(self,vars=None):
    self.variables = vars

  def fit(self,X,y=None):
    self.label_dict = {}
    for var in self.variables:
      unique_categories = X[var].unique()
      self.label_dict[var] = {cat: i for i,cat in enumerate(unique_categories)}
    return self

  def transform(self,X):
    for var in self.variables:
      X[var] = X[var].map(self.label_dict[var])
    return X


#Log transformation
class LogTransform:
    def __init__(self,vars=None):
        self.variables = vars

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        for var in self.variables:
            X[var] = np.log(X[var])
        return X