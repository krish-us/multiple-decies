# -- coding: utf-8 --
"""
Created on Mon Jun 23 10:26:00 2025

@author: Felix
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_model = pickle.load(open('heart_model.sav','rb'))
Park_model = pickle.load(open('Parkinson_model.sav','rb'))

# make a sidebar fro navigation 
with st.sidebar:
       selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )
       
# diabetes prediction page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')
    
    # input fields for diabetes prediction
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure Value')
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI Value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
        Age = st.text_input('Age of the Person')

    # prediction button
    if st.button('Diabetes Test Result'):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        input_data_as_float = [float(i) for i in input_data]
        input_data_reshaped = [input_data_as_float]
        
        prediction = diabetes_model.predict(input_data_reshaped)
        
        if prediction[0] == 0:
            st.success('The person is not diabetic.')
        else:
            st.error('The person is diabetic.')

# heart diaseaes
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')
    
    # input fields for diabetes prediction
    col1, col2,col3 ,col4= st.columns(4)
    
    with col1:
        age = st.text_input('Enter Age')
        sex = st.text_input('Gender (0 = female, 1 = male)')
        cp = st.text_input('Enter Chest Pain Type (cp)')
        trestbps = st.text_input('Enter Resting Blood Pressure (trestbps)')
        
    with col2:
        chol = st.text_input('Enter Cholesterol Level')
        fbs = st.text_input('Fasting Blood Sugar (0 = false; 1 = true)')
        restecg = st.text_input('Resting ECG Results')
        thalach = st.text_input('Maximum Heart Rate Achieved')
    
    with col3:
        exang = st.text_input('Exercise  (0 = no; 1 = yes)')
        oldpeak = st.text_input('ST Depression Induced by Exercise')
        slope = st.text_input('Slope of the Peak Exercise')
        thal = st.text_input('Thal (1 = normal; 2 = fixed defect; 3 = reversible defect)')
    
    with col4:
        
        ca = st.text_input('No. of Major Vessels (0–3)')
    # prediction button
    if st.button('Diabetes Test Result'):
        input_data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        input_data_as_float = [float(i) for i in input_data]
        input_data_reshaped = [input_data_as_float]
        
        prediction = heart_model.predict(input_data_reshaped)
        if prediction[0] == 0:
            st.success('The person does NOT have a heart disease.')
        else:
            st.error('The person HAS a heart disease.')

# parkinsons prediction page
# ── Parkinson’s Prediction ───────────────────────────────────────────
if selected == "Parkinsons Prediction":
    st.title("Parkinson’s Prediction")

    # five equal columns for compact input layout
    col1, col2, col3, col4, col5 = st.columns(5)

    # ── Column-wise inputs (23 numeric fields) ────────────────────────
    with col1:
        name            = st.text_input("Patient ID (numeric)")
        fo              = st.text_input("MDVP:Fo(Hz)")
        fhi             = st.text_input("MDVP:Fhi(Hz)")
        flo             = st.text_input("MDVP:Flo(Hz)")
        jitter_percent  = st.text_input("MDVP:Jitter(%)")

    with col2:
        jitter_abs      = st.text_input("MDVP:Jitter(Abs)")
        rap             = st.text_input("MDVP:RAP")
        ppq             = st.text_input("MDVP:PPQ")
        ddp             = st.text_input("Jitter:DDP")
        shimmer         = st.text_input("MDVP:Shimmer")

    with col3:
        shimmer_db      = st.text_input("MDVP:Shimmer(dB)")
        apq3            = st.text_input("Shimmer:APQ3")
        apq5            = st.text_input("Shimmer:APQ5")
        apq             = st.text_input("MDVP:APQ")
        dda             = st.text_input("Shimmer:DDA")

    with col4:
        nhr             = st.text_input("NHR")
        hnr             = st.text_input("HNR")
        rpde            = st.text_input("RPDE")
        dfa             = st.text_input("DFA")
        spread1         = st.text_input("Spread1")

    with col5:
        spread2         = st.text_input("Spread2")
        d2              = st.text_input("D2")
        ppe             = st.text_input("PPE")

    # ── Run prediction ────────────────────────────────────────────────
    if st.button("Parkinsons Test Result"):
        try:
            # assemble list in the exact order expected by the model
            features = [
                name, fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
                shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde,
                dfa, spread1, spread2, d2, ppe
            ]
            input_data = [float(x) for x in features]  # convert ➜ float
            prediction = Park_model.predict([input_data])  # model must be loaded earlier

            if prediction[0] == 0:
                st.success("The person does *NOT* have Parkinson’s disease.")
            else:
                st.error("The person *HAS* Parkinson’s disease.")
        except ValueError:
            st.warning("❗ Please fill *every* field with a numeric value.")
