import pathlib
import os
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
#print(str(pathlib.Path(__file__).resolve().parents[2]))

import prediction_model

#PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parents[1]
#print("Root Package-",PACKAGE_ROOT)

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")
#print("Location of data files-",DATAPATH)

TRAIN_FILE = 'loanTrain.csv'
TEST_FILE = 'test_loan.csv'

MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,"trained_models")
#print("Model save location-", SAVE_MODEL_PATH )

TARGET = 'Loan_Status'
FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
            'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 
            'LoanAmount','Loan_Amount_Term', 'Credit_History', 'Property_Area']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount','Loan_Amount_Term']
CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education','Self_Employed',
                'Credit_History', 'Property_Area']

FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education',
                      'Self_Employed', 'Property_Area']

FEATURES_TO_MODIFY = ['ApplicantIncome']
FEATURES_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = 'CoapplicantIncome'

LOG_FEATURES =  ['ApplicantIncome', 'LoanAmount','Loan_Amount_Term']

