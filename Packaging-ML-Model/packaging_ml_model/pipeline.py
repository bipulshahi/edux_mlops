from sklearn.pipeline import Pipeline

import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from packaging_ml_model.config import config

import packaging_ml_model.processing.preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np


#pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])

classification_pipeline = Pipeline([
    ('Mean Imputation', pp.MeanImputer(config.NUM_FEATURES)),
    ('Mode Imputation' , pp.ModeImputer(config.CAT_FEATURES)),
    ('DomainProcessing' , pp.DomainProcessing(variables_to_modify=config.FEATURE_TO_MODIFY,
                                              variables_to_add=config.FEATURES_TO_ADD)),
    ('Drop Features' , pp.DropColumns(config.DROP_FEATURES)),
    ('LabelEncoder' , pp.CustomLabelEncoder(config.FEATURE_TO_ENCODE)),
    ('LogTransform' , pp.LogTransform(config.LOG_FEATURES)),
    ('MinMaxScale', MinMaxScaler()),
    ('LogisticClassifier', LogisticRegression())
])
