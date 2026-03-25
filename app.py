import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Customer Churn Prediction")

credit_score = st.number_input("Credit Score", 300, 900)
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 18, 100)
tenure = st.number_input("Tenure (Years)", 0, 10)
balance = st.number_input("Balance")
num_products = st.number_input("Number of Products", 1, 4)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary")

geo_dict = {"France": 0, "Spain": 1, "Germany": 2}
geography = geo_dict[geography]

gender = 1 if gender == "Male" else 0

if st.button("Predict"):

    data = np.array([[credit_score,geography,gender,age,tenure,balance,num_products,
has_cr_card,is_active,salary]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer will churn")
    else:
        st.success("Customer will stay")
