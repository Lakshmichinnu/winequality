import streamlit as st
import pickle


model=pickle.load(open("C:\\Users\\91799\\OneDrive\\Desktop\\ML_PROJECTS\\winequality\\winequality\\winequality",'rb'))

st.header("WINE QUALITY PREDICTION USING ML")
st.subheader(" ")
col1,col2,col3=st.columns(3)
with col1:
    fixed_acidity=st.number_input("Fixed Acidity")
    residual_sugar=st.number_input("Residual Sugar")
    total_sulfr_dioxide=st.number_input("Total Sulfur Dioxide")
    sulphates=st.number_input("Sulphates")
with col2:
    volatile_acidity=st.number_input("Volatile Acidity")
    chlorides=st.number_input("Chlorides")
    density=st.number_input("Density")
    alcohol=st.number_input("Alcohol")
with col3:
    citric_acid=st.number_input("Citric Acid")
    free_sulfr_dioxide=st.number_input("Free Sulfur Dioxide")
    ph=st.number_input("PH")

quality_predition=""

st.subheader("")

if st.button("CHECK QUALITY"):
    prediction=model.predict([[fixed_acidity,volatile_acidity,citric_acid,
                               residual_sugar,chlorides,free_sulfr_dioxide,
                               total_sulfr_dioxide,density,ph,sulphates,alcohol]])

    if (prediction[0]==1):
        quality_predition="GOOD QUALITY WINE"
        st.balloons()
    else:
        quality_predition="BAD QUALITY WINE"

st.subheader("")
st.success(quality_predition)

