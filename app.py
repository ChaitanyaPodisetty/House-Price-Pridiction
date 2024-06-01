import streamlit as st
import requests
import pickle
import io

st.header("House-Price Prediction")

with open('data.pkl', 'rb') as file:
    # Load the content of the pickle file
    file_content = file.read()

with open('model.pkl', 'rb') as file:
    # Load the content of the pickle file
    file_content = file.read()
#pickle.loads(open('data.pkl','rb'))
#pickle.loads(open('model.pkl','rb'))

model = pickle.loads(file_content)

#input = st.text_input("MedInc")
#input = st.text_input("HouseAge")
#input = st.text_input("AveRooms")
#input = st.text_input("AveBedrms")
#input = st.text_input("Population")
#input = st.text_input("AveOccup")
#input = st.text_input("Latitude")
#input = st.text_input("Longitude")


# Display some output based on the input

medinc_input = st.text_input("MedInc")
houseage_input = st.text_input("HouseAge")
averooms_input = st.text_input("AveRooms")
avebedrms_input = st.text_input("AveBedrms")
population_input = st.text_input("Population")
aveoccup_input = st.text_input("AveOccup")
latitude_input = st.text_input("Latitude")
longitude_input = st.text_input("Longitude")

submit = st.button("Get Price")

# Prediction logic
if submit:
    # Convert inputs to appropriate data types
    medinc = float(medinc_input)
    houseage = float(houseage_input)
    averooms = float(averooms_input)
    avebedrms = float(avebedrms_input)
    population = float(population_input)
    aveoccup = float(aveoccup_input)
    latitude = float(latitude_input)
    longitude = float(longitude_input)

    # Make predictions
    features = [[medinc, houseage, averooms, avebedrms, population, aveoccup, latitude, longitude]]
    price = model.predict(features)

    st.write("Predicted Price:", price)

