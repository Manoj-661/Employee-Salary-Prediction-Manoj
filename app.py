import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and encoders
model = joblib.load("best_model.pkl")


# Recreate the LabelEncoders with the same classes used in training
education_encoder = joblib.load("education_encoder.pkl")
occupation_encoder = joblib.load("occupation_encoder.pkl")

# Streamlit UI
st.set_page_config(page_title="Employee Salary Predictor", layout="centered")
st.title("💼 Employee Salary Prediction App")
st.markdown("Predict whether an employee earns more than ₹50K based on input features")



# Inputs
age = st.slider("Age", 18, 65, 30)
education = st.selectbox("Education Level", education_encoder.classes_)
# ✅ Show original job roles in the dropdown (not numbers!)
occupation_options = list(occupation_encoder.classes_)
selected_occupation = st.selectbox("Job Role", occupation_options)
occupation = st.selectbox("Job Role", 
                          ["Tech-support",  "Other", "Craft-repair", 
                           "Other-service", "Sales","Exec-managerial", "Prof-specialty", "Handlers-cleaners",
                           "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv",
                           "Machine-op-inspct","Protective-serv", "Armed-Forces"])

# Encode selected role back to number
occ_encoded = occupation_encoder.transform([selected_occupation])[0]

hours = st.slider("Hours Worked Per Week", 1, 80, 40)
experience = st.slider("Years of Experience", 0, 40, 5)

# Encode categorical fields
edu_encoded = education_encoder.transform([education])[0]


# Prepare input as DataFrame
input_df = pd.DataFrame({
    'age': [age],
    'education': [edu_encoded],
    'occupation': [occ_encoded],
    'hours-per-week': [hours],
    'experiance': [experience],
    # Add other missing features here
    'feature6': [0],
    'feature7': [0],
    'feature8': [0],
    'feature9': [0],
    'feature10': [0],
    'feature11': [0],
    'feature12': [0]
})

# Prediction
if st.button("Predict Salary Class"):
    prediction = model.predict(input_df)[0]
    result = "≥ ₹50K" if prediction == 1 else "≤ ₹50K"
    st.success(f"🧾 Predicted Salary Class: **{result}**")
