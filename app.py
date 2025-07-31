import streamlit as st
import numpy as np
import joblib

st.markdown("""
    <style>
        .stApp {
            background: radial-gradient(circle at center, #14532d, #0e1117);
            background-attachment: fixed;
        }
    </style>""", unsafe_allow_html=True)



# Load model
model = joblib.load("Farm_Irrigation_System.pkl")

# Page config
st.set_page_config(page_title="Smart Irrigation", page_icon="💧", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>💧 Smart Irrigation Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter sensor values (0–1) to predict sprinkler status for each parcel.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input section in two columns for better UX
sensor_inputs = []
for i in range(0, 20, 2):
    col1, col2 = st.columns(2)
    with col1:
        val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, step=0.1, value=0.5)
        sensor_inputs.append(val)
    with col2:
        val = st.slider(f"Sensor {i+1}", min_value=0.0, max_value=1.0, step=0.1, value = 0.5)
        sensor_inputs.append(val)

# Predict button
if st.button("🚀 Predict Irrigation"):
    input_array = np.array(sensor_inputs).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("---")
    st.subheader("📊 Prediction Result")
    
    for i, status in enumerate(prediction):
        if status == 1:
            st.success(f"✅ Sprinkler {i} (Parcel {i}): ON")
        else:
            st.error(f"❌ Sprinkler {i} (Parcel {i}): OFF")

