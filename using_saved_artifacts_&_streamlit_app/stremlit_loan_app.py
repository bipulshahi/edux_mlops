import streamlit as st
import numpy as np
import joblib

#read the artifacts to make predictions
try:
    _model = joblib.load('E:/edux_mlops_dir/use_saved_file/loan_approval_model.pkl')
    _scaler = joblib.load('E:/edux_mlops_dir/use_saved_file/loan_approval_scaler.pkl')
except Exception as err:
    st.error(f"Error loading model - {err}")
    st.stop()


#function to be triggered when a user clicked on predict button
def predict(gender,married,dependents,education,self_employed,applicant_income,
            coapplicant_income,loan_amount,loan_amount_term,credit_history,property_area):
    
    #on accepting the user input convert it into the numerical form as it was used during training
    gen_encode = lambda x : 0 if x == "Female" else 1
    married_encode = lambda x : 0 if x == "No" else 1
    dependents_encode = lambda x : 0 if x == "0" else 1 if x == "1" else 2 if x == "2" else 3
    edu_encode = lambda x : 0 if x == 'Not Graduate' else 1
    self_employed_encode = lambda x : 0 if x == "No" else 1
    prop_area_encode = lambda x : 0 if x == 'Rural' else 1 if x == 'Semiurban' else 2


    Gender = gen_encode(gender)
    Married = married_encode(married)
    Dependents = dependents_encode(dependents)
    Education = edu_encode(education)
    Self_employed = self_employed_encode(self_employed)
    Property_area = prop_area_encode(property_area)

    Applicant_income = applicant_income + coapplicant_income

    Applicant_income_log = np.log(Applicant_income)
    Loan_amount_log = np.log(loan_amount)
    Loan_amount_term_log = np.log(loan_amount_term)

    #use the transformed data to for scaling
    prediction_data = _scaler.transform([[Gender,Married,Dependents,Education,
                                     Self_employed,Applicant_income_log,Loan_amount_log,
                                     Loan_amount_term_log,credit_history,Property_area]])
    
    #use the scaled data to predict and return predicted value
    return _model.predict(prediction_data)[0]



#streamlit app
def main():
    st.title("Welcome to Loan Application")
    st.header("Please fill your details to proceed for loan application-")

    gender = st.selectbox("Gender" , ["Male","Female"])
    married = st.selectbox("Married" , ["Yes","No"])
    dependents = st.selectbox("Dependents" , ['0', '1','2', '3+'])
    education = st.selectbox("Education" , ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Self Employed" , ['No', 'Yes'])
    applicant_income = st.number_input("Applicant Income")
    coapplicant_income = st.number_input("Co-Applicant Income")
    loan_amount = st.number_input("Loan Amount")
    loan_amount_term = st.number_input("Loan Amount Term")
    credit_history = st.number_input("Credit History")
    property_area = st.selectbox("Property Area" , ['Urban', 'Rural', 'Semiurban'])

    if st.button("Predict"):
        result = predict(gender,married,dependents,education,self_employed,applicant_income,
                         coapplicant_income,loan_amount,loan_amount_term,credit_history,property_area)
        if result == 1:
            st.success("Application Status: - Approved")
        else:
            st.error("Application Status - Not Approved")



if __name__ == "__main__":
    main()