import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Student Marks Predictor",
    page_icon="🎓",
    layout="centered"
)

model = joblib.load("student_marks_model.pkl")

st.title("🎓 Student Marks Predictor")
st.write("Enter student information below to predict final marks.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    study_hours = st.number_input(
        "📚 Study Hours",
        min_value=0.0,
        max_value=24.0,
        value=5.0
    )

with col2:
    attendance = st.number_input(
        "📅 Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

with col3:
    previous_marks = st.number_input(
        "📝 Previous Marks",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

st.divider()

if st.button("🔮 Predict Marks"):
    new_student = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Marks": [previous_marks]
    })

    prediction = model.predict(new_student)

    final_marks = max(0, min(100, prediction[0]))
    st.success(f"🎯 Predicted Final Marks: {final_marks:.2f}")

    if final_marks >= 80:
        st.info("🌟 Excellent Performance")
    elif final_marks >= 70:
        st.info("👍 Very Good Performance")
    elif final_marks >= 60:
        st.info("📈 Good Performance")
    elif final_marks >= 50:
        st.warning("📚 Needs Improvement")
    else:
        st.warning("💪 Needs More Study")
        st.divider()

st.subheader("📊 Model Performance")

st.write("The model was evaluated on unseen test data.")

col1, col2 = st.columns(2)

with col1:
    st.metric("MAE", "3.81 marks")

with col2:
    st.metric("R² Score", "0.7792")
    st.divider()

st.subheader("ℹ️ About This Project")

st.write(
    "This application uses a Linear Regression machine learning model "
    "to predict a student's final marks based on study hours, attendance, "
    "and previous marks."
)

st.caption("🎓 Student Marks Prediction | Machine Learning Project | Created by Muhammad Hassan")