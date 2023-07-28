# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 23:36:52 2023

@author: madhu
"""
import numpy as np
import pickle
import streamlit as st
import sklearn
import os


path = os.path.dirname(__file__)
my_file = path+'/trained_model.pkl'

loaded_model = pickle.load(open(my_file, 'rb'))

#creating a function for prediction
def loan_prediction(input_data) :
    prediction = loaded_model.predict(input_data)      

    if(prediction[0]==0):
        return "I am sorry, you can't get loan."
    else :
        return "Congratulations,you can get loan."


def main():
    # Giving a title
    st.title('Loan Status Prediction Web App')

    # Getting input data from the user
    Gender = st.selectbox('Please choose your Gender', ('Male', 'Female'))
    gender = 1 if Gender == 'Male' else 0

    Dependents = st.number_input('Dependents', min_value=0, max_value=15)

    Married = st.selectbox('Are you married?', ('Yes', 'No'))
    married = 1 if Married == 'Yes' else 0

    Education = st.selectbox('Education', ('Graduate', 'Not Graduate'))
    education = 0 if Education == 'Graduate' else 1

    Self_Employed = st.selectbox('Are you self-employed?', ('Yes', 'No'))
    self_employed = 1 if Self_Employed == 'Yes' else 0

    ApplicantIncome = st.number_input('Applicant Income', min_value=100, max_value=100000)

    CoapplicantIncome = st.number_input('Co-applicant Income', min_value=0, max_value=50000)

    LoanAmount = st.number_input('Loan Amount', min_value=1, max_value=1000)

    Loan_Amount_Term = st.number_input('Loan Amount Term (days)', min_value=10, max_value=480)

    Credit_History = st.selectbox('Do you have any Credit History?', ('Yes', 'No'))
    credit_history = 1 if Credit_History == 'Yes' else 0

    Property_Area = st.selectbox('Property Area', ('Urban', 'Semi Urban', 'Rural'))
    property_area = 2 if Property_Area == 'Urban' else 1 if Property_Area == 'Semi Urban' else 0

    # Code for prediction
    availability = ''

    # Creating a button for prediction
    if st.button('Loan Availability Test Result'):
        availability = loan_prediction([[gender, Dependents, married, education, self_employed, ApplicantIncome,
                                      CoapplicantIncome, LoanAmount, Loan_Amount_Term, credit_history, property_area]])


    st.success(availability)
        
        
        
if __name__ == "__main__":
    main()
    

    
    