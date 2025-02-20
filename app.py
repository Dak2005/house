import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("flat_price_model.pkl")

# Streamlit UI
st.title("Flat Price Prediction in Hyderabad")

# User inputs
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
kitchens = st.number_input("Number of Kitchens", min_value=1, max_value=5, value=1)
square_feet = st.number_input("Square Feet", min_value=500, max_value=100000, value=1000)
car_parking = st.selectbox("Car Parking", ["Yes", "No"])
floor_number = st.number_input("Floor Number", min_value=1, max_value=50, value=1)
age_of_property = st.number_input("Age of Property (years)", min_value=0, max_value=100, value=5)
location = st.selectbox("Location", ["Hitech City", "Kukatpally", "Gachibowli", "Banjara Hills", "Mehdipatnam","Madhapur","Begumpet","Jubilee Hills","Kondapur","Manikonda"])

# Prediction
if st.button("Predict Price"):
    # Prepare the input data
    input_data = pd.DataFrame([[bedrooms, bathrooms, kitchens, square_feet, car_parking, floor_number, age_of_property, location]],
                              columns=['bedrooms', 'bathrooms', 'kitchens', 'square_feet', 'car_parking', 'floor_number', 'age_of_property', 'location'])

    # Make prediction
    predicted_price = model.predict(input_data)[0]

    st.success(f"Estimated Flat Price: ₹{predicted_price:.2f} Lakhs")
