import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("best_rf_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🩺 Cancer Survival Prediction App")
st.write("Enter full patient information to predict survival outcome")

# Input fields (based on your Cleaned_Train.csv)

# Numerical
tumor_size = st.slider("Tumor Size (mm)", 0, 200, 30)
cost = st.number_input("Healthcare Costs", value=1000.0)
insurance_cost = st.number_input("Insurance Costs", value=800.0)
incidence_rate = st.slider("Incidence Rate per 100K", 0, 1000, 150)
mortality_rate = st.slider("Mortality Rate per 100K", 0, 1000, 100)

# Categorical / Binary
birth_year = st.slider("Year of Birth", 1930, 2020, 1980)
alcohol = st.selectbox("Alcohol Consumption", ["None", "Moderate", "High"])
cancer_stage = st.selectbox("Cancer Stage", ["I", "II", "III", "IV"])
country = st.text_input("Country (use code or label)", "USA")
diabetes = st.radio("Diabetes", ["Yes", "No"])
diabetes_history = st.radio("Diabetes History", ["Yes", "No"])
diet_risk = st.radio("Diet Risk", ["Yes", "No"])
early_detection = st.radio("Early Detection", ["Yes", "No"])
family_history = st.radio("Family History", ["Yes", "No"])
gender = st.radio("Gender", ["Male", "Female"])
genetic = st.radio("Genetic Mutation", ["Yes", "No"])
health_access = st.selectbox("Healthcare Access", ["Good", "Limited"])
heart_disease = st.radio("Heart Disease History", ["Yes", "No"])
hypertension = st.radio("Hypertension", ["Yes", "No"])
ibd = st.radio("Inflammatory Bowel Disease", ["Yes", "No"])
insurance_status = st.radio("Insurance Status", ["Insured", "Uninsured"])
non_smoker = st.radio("Non Smoker", ["Yes", "No"])
obesity = st.selectbox("Obesity BMI", ["Underweight", "Normal", "Obese"])
physical_activity = st.selectbox("Physical Activity", ["Low", "Moderate", "High"])
screening = st.radio("Screening History", ["Yes", "No"])
smoking = st.radio("Smoking History", ["Yes", "No"])
transfusion = st.radio("Transfusion History", ["Yes", "No"])
treatment = st.selectbox("Treatment Type", ["Chemotherapy", "Surgery", "Immunotherapy"])
urban_rural = st.radio("Urban or Rural", ["Urban", "Rural"])

# Encode categorical values (must match training logic!)
encoded = np.array([[
    {"None": 0, "Moderate": 1, "High": 2}[alcohol],
    {"I": 1, "II": 2, "III": 3, "IV": 4}[cancer_stage],
    2025 - birth_year,  # Approximate age
    1 if diabetes == "Yes" else 0,
    1 if diabetes_history == "Yes" else 0,
    1 if diet_risk == "Yes" else 0,
    1 if early_detection == "Yes" else 0,
    1 if family_history == "Yes" else 0,
    1 if gender == "Male" else 0,
    1 if genetic == "Yes" else 0,
    1 if health_access == "Good" else 0,
    cost,
    1 if heart_disease == "Yes" else 0,
    1 if hypertension == "Yes" else 0,
    incidence_rate,
    1 if ibd == "Yes" else 0,
    insurance_cost,
    1 if insurance_status == "Insured" else 0,
    mortality_rate,
    1 if non_smoker == "Yes" else 0,
    {"Underweight": 0, "Normal": 1, "Obese": 2}[obesity],
    {"Low": 0, "Moderate": 1, "High": 2}[physical_activity],
    1 if screening == "Yes" else 0,
    1 if smoking == "Yes" else 0,
    1 if transfusion == "Yes" else 0,
    {"Chemotherapy": 0, "Surgery": 1, "Immunotherapy": 2}[treatment],
    tumor_size,
    1 if urban_rural == "Urban" else 0
]])

# Scale input and predict
input_scaled = scaler.transform(encoded)
prediction = model.predict(input_scaled)[0]

# Output result
st.subheader("Prediction Result")
st.success("✅ Survived" if prediction == 1 else "❌ Did Not Survive")