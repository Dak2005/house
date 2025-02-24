import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("flat_price_model.pkl")

# Set background image using CSS
background_image_url = "https://s7ap1.scene7.com/is/image/incredibleindia/charminar-mosque-hyderabad-telangana-3-attr-about?qlt=82&ts=1726652899615"

page_bg = f"""
<style>
body {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}}
.stApp {{
    background-color: rgba(0, 0, 0, 0.6); /* Dark overlay for readability */
    padding: 20px;
    border-radius: 10px;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Custom CSS for Styling
st.markdown("""
    <style>
        /* Title Styling */
        .title {
            color: #FFD700; /* Gold color */
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        
        /* Input field styles */
        div[data-testid="stNumberInput"] label, div[data-testid="stSelectbox"] label {
            color: #FF5733; /* Orange-Red */
            font-weight: bold;
        }

        /* Styling the number input boxes */
        div[data-testid="stNumberInput"] input {
            background-color: #222222; /* Dark Background */
            color: white;
            border-radius: 8px;
        }
        
        /* Styling the dropdown select box */
        div[data-testid="stSelectbox"] select {
            background-color: #222222;
            color: white;
            border-radius: 8px;
        }
        
        /* Custom button style */
        div[data-testid="stButton"] button {
            background-color: #008CBA; /* Blue */
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px;
        }

        /* Centered Button */
        .stButton {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.markdown('<p class="title">🏠 Flat Price Prediction in Hyderabad</p>', unsafe_allow_html=True)

# User inputs
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
kitchens = st.number_input("Number of Kitchens", min_value=1, max_value=5, value=1)
square_feet = st.number_input("Square Feet", min_value=500, max_value=100000, value=1000)
car_parking = st.selectbox("Car Parking", ["Yes", "No"])
floor_number = st.number_input("Floor Number", min_value=1, max_value=50, value=1)
age_of_property = st.number_input("Age of Property (years)", min_value=0, max_value=100, value=5)
location = st.selectbox("Location", ["Hitech City", "Kukatpally", "Gachibowli", "Banjara Hills", "Mehdipatnam",
                                     "Madhapur", "Begumpet", "Jubilee Hills", "Kondapur", "Manikonda"])

# Prediction
if st.button("Predict Price"):
    # Prepare the input data
    input_data = pd.DataFrame([[bedrooms, bathrooms, kitchens, square_feet, car_parking, floor_number, age_of_property, location]],
                              columns=['bedrooms', 'bathrooms', 'kitchens', 'square_feet', 'car_parking', 'floor_number', 'age_of_property', 'location'])

    # Make prediction
    predicted_price = model.predict(input_data)[0]

    st.success(f"🏡 Estimated Flat Price: ₹{predicted_price:.2f} Lakhs")
