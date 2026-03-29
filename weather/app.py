import streamlit as st
import numpy as np
import pickle 
model=pickle.load(open("model.pkl","rb"))
st.title("WEATHER PREDICTION MODEL")
st.write("This is a weather prediction model which is trained on the basis of 6 features. It will predict whether it will snow or rain.")
Humidity=st.number_input("Humidity")
Wind_Speed=st.number_input("Wind Speed (km/h)")
Wind_Bearing=st.number_input("Wind Bearing (degrees)")
Visibility=st.number_input("Visibility (km)")
Loud_Cover=st.number_input("Loud Cover")
Pressure=st.number_input("Pressure (millibars)")


if st.button("Predict"):
    input_data=np.array([[Humidity,Wind_Speed,Wind_Bearing,Visibility,Loud_Cover,Pressure]])
    prediction=model.predict(input_data)
    if prediction[0]==0:
        st.write("will snow")
    else:
        st.write("will rain")