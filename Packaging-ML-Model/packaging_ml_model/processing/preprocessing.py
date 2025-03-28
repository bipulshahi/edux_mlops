import numpy as np

#mean imputaion
class MeanImputer():
    def __init__(self,variables=None):
        self.variables = variables

    def fit(self,X,y=None):
        self.mean_dict = {}
        for var in self.variables:
            self.mean_dict[var] = X[var].mean()
        return self

    def transform(self,X):
        for var in self.variables:
            X[var] = X[var].fillna(self.mean_dict[var])
        return X


#mode imputation
class ModeImputer():
    def __init__(self,variables=None):
        self.variables = variables

    def fit(self,X,y=None):
        self.mode_dict = {}
        for var in self.variables:
            self.mode_dict[var] = X[var].mode()[0]
        return self

    def transform(self,X):
        for var in self.variables:
            X[var] = X[var].fillna(self.mode_dict[var])
        return X

#drop columns
class DropColumns():
    def __init__(self,variables=None):
        self.variables = variables

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        X = X.drop(columns = self.variables)
        return X

#domain specific preprocessing
class DomainProcessing():
    def __init__(self,variables_to_modify=None,variables_to_add=None):
        self.variables_to_modify = variables_to_modify
        self.variables_to_add = variables_to_add

    def fit(self,X,y=None):
        return self

    def transform(self,X):
        for var in self.variables_to_modify:
            X[var] = X[var] + X[self.variables_to_add]
        return X

#label encoding
class CustomLabelEncoder():
  def __init__(self,variables=None):
    self.variables = variables

  def fit(self,X,y=None):
    self.label_dict = {}
    for var in self.variables:
      t = X[var].unique()
      self.label_dict[var] = {cat : i for i,cat in enumerate(t)}           
    return self

  def transform(self,X):
    for var in self.variables:
      X[var] = X[var].map(self.label_dict[var])
    return X

#log transformation
class LogTransform():
    def __init__(self,variables=None):
        self.variables = variables

    def fit(self,X,y=None):
        return X

    def transform(self,X):
        for var in self.variables:
            X[var] = np.log(X[var])
        return X