import streamlit as st
import requests

st.title("LIVE CURRENCY CONVERTER")
st.subheader("Convert your currency in real-time")
amount = st.number_input("Enter amount in USD", min_value=0.0, format="%.2f")
target_currency = st.selectbox("Select currency", ["INR", "EUR", "GBP"])           

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    
    if target_currency in data['rates']:
        conversion_rate = data['rates'][target_currency]
        converted_amount = amount * conversion_rate
        st.success(f"{amount} USD is equal to {converted_amount:.2f} {target_currency}")
    else:
        st.error("Currency not supported")
