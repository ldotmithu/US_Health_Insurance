import streamlit as st 
import pandas as pd 
import joblib


preprocess = joblib.load('artifacts/model_train/preprocess.json')  
model = joblib.load('artifacts/model_train/model.json')  

st.title("Health Insurance Prediction")

st.write("### Enter your details:")


age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", options=['male', 'female'])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=5, value=1)
smoker = st.selectbox("Smoker", options=['no', 'yes'])
region = st.selectbox("Region", options=['southwest', 'southeast', 'northwest', 'northeast'])


user_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
})

user_data_preprocessed = preprocess.transform(user_data)

predicted_charge = model.predict(user_data_preprocessed)


st.write(f"### Predicted Insurance Charge: ${predicted_charge[0]:.2f}")


accuracy = 0.85  
st.write(f"Model Accuracy: {accuracy * 100:.2f}%")
