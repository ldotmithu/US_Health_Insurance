import streamlit as st 
import pandas as pd 
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load preprocessing and model
preprocess = joblib.load('artifacts/model_train/preprocess.pkl')  
model = joblib.load('artifacts/model_train/model.pkl')  

# Title and description
st.title("Health Insurance Prediction")
st.write("### Enter your details:")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", options=['male', 'female'])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=5, value=1)
smoker = st.selectbox("Smoker", options=['no', 'yes'])
region = st.selectbox("Region", options=['southwest', 'southeast', 'northwest', 'northeast'])

# Submit button to trigger prediction
if st.button('Submit'):
    # Prepare user data
    user_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })

    # Preprocess the data
    user_data_preprocessed = preprocess.transform(user_data)

    # Get prediction
    predicted_charge = model.predict(user_data_preprocessed)

    # Display the predicted charge
    st.write(f"### Predicted Insurance Charge: ${predicted_charge[0]:.2f}")
