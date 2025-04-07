from sklearn.pipeline import Pipeline

import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from prediction_model.config import config
import prediction_model.processing.preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import numpy as np


#pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])

classification_pipeline = Pipeline([
    ('Mean Imputation' , pp.MeanImputer(config.NUM_FEATURES)),
    ('Mode Imputation' , pp.ModeImputer(config.CAT_FEATURES)),
    ('Domain Processing' , pp.DomainProcessing(vars_to_modify=config.FEATURES_TO_MODIFY,
                                               vars_to_add=config.FEATURES_TO_ADD)),
    ('Drop Features' , pp.DropColumns(vars_to_drop=config.DROP_FEATURES)),
    ('Label Encoder' , pp.CustomLabelEncoder(config.FEATURES_TO_ENCODE)),
    ('Log Transform' , pp.LogTransform(config.LOG_FEATURES)),
    ('MinMaxScale' , MinMaxScaler()),
    ('Support vector Classifier' , SVC())
])