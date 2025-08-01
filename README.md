# AICTE-Internship
This Internship aims to focus on Green skills with AI and addressing to real world problems with best solution through ideation and innovation in technology 


# 🌿 Smart Irrigation System using Machine Learning

A Smart Irrigation System built during the AICTE internship that uses sensor data to predict the ON/OFF status of 3 irrigation pumps using a machine learning model. This system promotes green skills and sustainable farming through AI-based automation.

---

## 📌 Project Description

This project utilizes a dataset containing readings from 20 environmental sensors and the corresponding status of 3 irrigation pumps. A machine learning model (Random Forest) is trained to predict pump operation based on the sensor values. The trained model is deployed using a Streamlit web application, allowing users to input sensor readings and view real-time pump predictions.

---

## ✅ Prerequisites

Ensure you have Python 3.7+ inst packages
└── README.md # Project overview and instructions



---

## ✅ Prerequisites

Ensure you have Python 3.7+ installed. Then install required packages:

```bash
pip install numpy
pip install panadas 
pip install skitlearn
pip install joblib

```
--- 
# 🧪 How to Run the Jupyter Notebook

1. Open the file Smart_irrigation_Aicte.ipynb in Jupyter Notebook or Google Colab.
2. Run all cells to:

    - Load and preprocess the data
    - Train the MultiOutputClassifier using RandomForest
    - Evaluate the model
    - Save the trained model as Farm_Irrigation_System.pkl

Make sure the dataset file irrigation_machine.csv is in the same directory.

---

# 🚀 How to Run the Streamlit App
1. Ensure the model file Farm_Irrigation_System.pkl is present in the same folder as app.py.
2. Start the app

```bash
streamlit run app.py
```

3. The web app will open in your default browser. You can:

- Enter values for each of the 20 sensors using sliders.
- Click "Predict Pump Status".
- View ON/OFF predictions for the 3 pumps

# 🌱 Green Skills & Innovation
1. Promotes water conservation and sustainable irrigation.
2. Encourages data-driven decision-making in agriculture.
3. Demonstrates practical integration of AI for environmental benefit
