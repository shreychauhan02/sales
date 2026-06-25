import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

st.title("Customers")

name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")

if st.button("Add Customer"):

    data = {
        "name": name,
        "phone_number": phone
    }

    requests.post(
        f"{API}/customers/",
        json=data
    )

    st.success("Customer Added")

st.divider()

customers = requests.get(
    f"{API}/customers/"
).json()

st.dataframe(
    pd.DataFrame(customers),
    use_container_width=True
)