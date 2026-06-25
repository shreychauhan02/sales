import streamlit as st
import requests
import pandas as pd
from datetime import date

API = "http://127.0.0.1:8000"

st.title("Orders")

order_date = st.date_input(
    "Order Date",
    value=date.today()
)

price = st.number_input(
    "Total Price",
    min_value=0
)

status = st.selectbox(
    "Status",
    [
        "pending",
        "completed"
    ]
)

customer = st.number_input(
    "Customer ID",
    min_value=1
)

employee = st.number_input(
    "Employee ID",
    min_value=1
)

if st.button("Create Order"):

    data = {
        "order_date": str(order_date),
        "total_price": price,
        "status": status,
        "cus_id": customer,
        "emp_id": employee
    }

    requests.post(
        f"{API}/orders/",
        json=data
    )

    st.success("Order Created")

st.divider()

orders = requests.get(
    f"{API}/orders/"
).json()

st.dataframe(
    pd.DataFrame(orders),
    use_container_width=True
)