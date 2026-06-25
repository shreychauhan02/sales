import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

st.title("Products")

name = st.text_input("Product Name")
category = st.number_input(
    "Category ID",
    min_value=1
)

price = st.number_input(
    "Price",
    min_value=0
)

stock = st.number_input(
    "Stock",
    min_value=0
)

if st.button("Add Product"):

    data = {
        "p_name": name,
        "category_id": category,
        "price": price,
        "stock": stock
    }

    requests.post(
        f"{API}/products/",
        json=data
    )

    st.success("Product Added")

st.divider()

products = requests.get(
    f"{API}/products/"
).json()

st.dataframe(
    pd.DataFrame(products),
    use_container_width=True
)