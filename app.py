import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open(r"F:\projects\diabetes_prediction\model.sav", "rb"))


# Function to predict diabetes
def predict_diabetes(data):
    data = np.asarray(data).reshape(1, -1)
    prediction = model.predict(data)

    if prediction[0] == 1:
        return "🔴 The person is Diabetic"
    else:
        return "🟢 The person is Not Diabetic"


# Main function
def main():

    st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺")

    st.title("🩺 Diabetes Prediction System")
    st.write("Enter the patient's details below.")

    pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function", min_value=0.0, format="%.3f"
    )
    age = st.number_input("Age", min_value=1)

    if st.button("Predict"):

        input_data = [
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age,
        ]

        result = predict_diabetes(input_data)

        if "Diabetic" in result:
            st.error(result)
        else:
            st.success(result)


# Run the app
if __name__ == "__main__":
    main()
