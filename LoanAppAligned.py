import streamlit as st
import pickle
from PIL import Image
import numpy as np


st.title("Loan Prediction APP")
img = Image.open("./stremlitexercises/loan3.jpeg")
st.image(img)
st.write("""The Loan Prediction Web Application is a web-based tool that predicts loan approval based on user input. It utilizes a machine learning model to provide an estimated outcome for loan applications. This project aims to assist individuals and 
         financial institutions in making informed decisions regarding loan approvals.""")
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender: ", ['Male', 'Female'], placeholder="Select the gender", index=None)
    married = st.selectbox("Marital Status: ", ['Married','Unmarried'], placeholder="Select the Marital status", index=None)
    dependents = st.number_input('Dependents', 0,5, placeholder = "Enter the no of dependents", value = None)
    education = st.selectbox("Education: ", ['Graduate','Not graduate'], placeholder="Select the Education status", index=None)
    employed = st.selectbox("Self-Employed: ", ['Yes','No'], placeholder="Select whether employed or not", index=None)
with col2:
    applicantincome =  st.number_input('Applicant Income', placeholder = "Enter the applicant income", value = None, min_value = 0)
    coapplicantincome =  st.number_input('Co-Applicant Income', placeholder = "Give coapplicant income", value = None, min_value = 0)
    loanamount =  st.number_input('Loan Amount', placeholder = "Enter the Loan Amount", value = None, min_value = 0)
    loanamountterm = st.number_input('Loan Amount Term', placeholder = "Enter the Loan Amount Term", value = None, min_value = 0)
    credithistory = st.selectbox("Whether having good credit history: ", ['Yes','No'], placeholder="Select the credit status", index=None)
propertyarea = st.selectbox("Property Area: ", ['Rural','Semiurban','Urban'], placeholder="Select the property area", index=None)

gender = 1 if gender == 'Male' else 0
married = 1 if married  == 'Married' else 0
education = 1 if education == 'Not graduate' else 0
employed = 1 if employed == 'Yes' else 0
credithistory = 1 if credithistory == 'Yes' else 0

if propertyarea == 'Rural':
    propertyarea = 0
elif propertyarea == 'Semiurban':
    propertyarea = 1
else:
    propertyarea = 2

inputdata = [gender,married,dependents,education,employed,applicantincome,coapplicantincome,loanamount,loanamountterm,credithistory,propertyarea]

print(inputdata)
def predictLoan (inputdata):
    model = pickle.load(open('/home/dell/pythonDA/Practicals/models/loanmodel.pkl','rb'))
    input_data_arr = np.array(inputdata).reshape(1,-1)
    loanstatus = model.predict(input_data_arr)
    if loanstatus == 1:
        st.success("Yes, Loan can be Aprroved")
    else:
        st.error("No, Loan Cannot be approved")

if(st.button("Predict")):
    predictLoan(inputdata)

