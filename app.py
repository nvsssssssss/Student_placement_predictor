import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# Load model + encoders
# ---------------------------
model = joblib.load("model.pkl")
feature_encoders = joblib.load("encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")

st.title("Student Placement Predictor")
st.write("Enter student details to predict placement status.")

# ---------------------------
# Input form (13 features, matching train.csv)
# ---------------------------
with st.form("prediction_form"):
    student_id = st.number_input("Student ID (any placeholder number)", min_value=1, value=99999)
    age = st.number_input("Age", min_value=18, max_value=24, value=21)
    gender = st.selectbox("Gender", ["Male", "Female"])
    degree = st.selectbox("Degree", ["B.Tech", "BCA", "MCA", "B.Sc"])
    branch = st.selectbox("Branch", ["CSE", "IT", "ECE", "ME", "Civil"])
    cgpa = st.number_input("CGPA", min_value=4.5, max_value=9.8, value=7.0, step=0.01)
    internships = st.number_input("Internships", min_value=0, max_value=3, value=1)
    projects = st.number_input("Projects", min_value=1, max_value=6, value=3)
    coding_skills = st.slider("Coding Skills", min_value=1, max_value=10, value=5)
    communication_skills = st.slider("Communication Skills", min_value=1, max_value=10, value=5)
    aptitude_test_score = st.number_input("Aptitude Test Score", min_value=35, max_value=100, value=60)
    soft_skills_rating = st.slider("Soft Skills Rating", min_value=1, max_value=10, value=5)
    certifications = st.number_input("Certifications", min_value=0, max_value=3, value=1)
    backlogs = st.number_input("Backlogs", min_value=0, max_value=3, value=0)

    submitted = st.form_submit_button("Predict")

# ---------------------------
# Prediction
# ---------------------------
if submitted:
    input_dict = {
        "Student_ID": student_id,
        "Age": age,
        "Gender": gender,
        "Degree": degree,
        "Branch": branch,
        "CGPA": cgpa,
        "Internships": internships,
        "Projects": projects,
        "Coding_Skills": coding_skills,
        "Communication_Skills": communication_skills,
        "Aptitude_Test_Score": aptitude_test_score,
        "Soft_Skills_Rating": soft_skills_rating,
        "Certifications": certifications,
        "Backlogs": backlogs,
    }

    input_df = pd.DataFrame([input_dict])

    # Apply the same label encoders used during training (Gender, Degree, Branch)
    for col, encoder in feature_encoders.items():
        if col in input_df.columns:
            input_df[col] = encoder.transform(input_df[col])

    # Predict
    prediction = model.predict(input_df)
    predicted_label = target_encoder.inverse_transform(prediction)[0]

    # Show confidence if the model supports probability estimates
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_df)[0]
        confidence = max(proba) * 100
        st.success(f"Predicted Status: **{predicted_label}** ({confidence:.1f}% confidence)")
    else:
        st.success(f"Predicted Status: **{predicted_label}**")
