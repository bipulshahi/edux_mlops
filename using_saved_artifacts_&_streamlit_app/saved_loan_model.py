import joblib
import numpy as np

#read the artifacts to make predictions
_model = joblib.load('E:/edux_mlops_dir/use_saved_file/loan_approval_model.pkl')
_scaler = joblib.load('E:/edux_mlops_dir/use_saved_file/loan_approval_scaler.pkl')

gender = 0
married = 0
dependents = 0
education = 1
self_employed = 0
applicant_income = 5400
loan_amount = 135
loan_amount_term = 340
credit_history = 1.0
property_area = 2


#we did log transformation before training so do log transformation before prediction
applicant_income_log = np.log(applicant_income)
loan_amount_log = np.log(loan_amount)
loan_amount_term_log = np.log(loan_amount_term)

#as we did data scaling before training so do data scaling before prediction
prediction_data = _scaler.transform([[gender,married,dependents,education,
                                     self_employed,applicant_income_log,loan_amount_log,
                                     loan_amount_term_log,credit_history,property_area]])

print(_model.predict(prediction_data)[0])