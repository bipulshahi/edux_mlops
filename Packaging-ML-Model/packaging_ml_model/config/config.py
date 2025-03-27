import pathlib
import os
import sys

#print(pathlib.Path(__file__).resolve().parents[2])
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
import packaging_ml_model

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parents[1]
#print(PACKAGE_ROOT)

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")
#print(DATAPATH)

TRAIN_FILE = 'loanTrain.csv'
TEST_FILE = 'test_loan.csv'

MODEL_NAME = 'loan_classfication.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,"trained_models")
#print(SAVE_MODEL_PATH)


TARGET = 'Loan_Status'
FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 
            'Self_Employed','ApplicantIncome', 'CoapplicantIncome',
            'LoanAmount', 'Loan_Amount_Term', 'Credit_History',
            'Property_Area']

NUM_FEATURES = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 
                'Self_Employed', 'Credit_History' , 'Property_Area']

#in our case we encoded the categorical columns
FEATURE_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed' , 'Property_Area']

FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURES_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = 'CoapplicantIncome'

LOG_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
