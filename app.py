import streamlit as st
import numpy as np
import pickle


# Loading model
model = pickle.load(open("Linear_regressor.pkl", "rb"))


st.title('Car Price Prediction')


# Creating input fields for the form
present_price = st.number_input('Present Price (in lakhs)')
kms_driven = st.number_input('Kms Driven')
owner = st.number_input('Owner')
age = st.number_input('Age (in years)')

# Creating dropdown for fuel type
fuel_type = st.selectbox('Fuel Type', ('Petrol', 'Diesel'))

# Creating radio button for seller type
seller_type = st.radio('Seller Type', ('Individual', 'Dealer'))

# Creating radio button for transmission type
transmission = st.radio('Transmission', ('Manual', 'Automatic'))


# Creating a function to convert fuel type to binary values
def get_fuel_type(fuel_type):
    if fuel_type == 'Petrol':
        return 1, 0
    else:
        return 0, 1


# Creating a function to convert seller type to binary values
def get_seller_type(seller_type):
    if seller_type == 'Individual':
        return 1
    else:
        return 0


# Creating a function to convert transmission type to binary values
def get_transmission(transmission):
    if transmission == 'Manual':
        return 1
    else:
        return 0


# Creating a button to predict the car price
if st.button('Predict'):
    fuel_type_petrol, fuel_type_diesel = get_fuel_type(fuel_type)
    seller_type_individual = get_seller_type(seller_type)
    transmission_manual = get_transmission(transmission)
    
    prediction = model.predict([[present_price, kms_driven, owner, age, fuel_type_diesel,
                                  fuel_type_petrol, seller_type_individual, transmission_manual]])
    
    output = round(prediction[0], 2)

    if output < 0:
        st.error('Sorry you cannot sell this car')
    else:
        st.success('You can sell the car at {} Lakhs'.format(output))
