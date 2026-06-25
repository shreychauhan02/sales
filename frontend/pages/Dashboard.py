import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API = "http://127.0.0.1:8000"

st.title("📈 Dashboard")


products = requests.get(
    f"{API}/analytics/top-products"
).json()

if products:

    df = pd.DataFrame(products)

    st.subheader("Top Selling Products")

    fig = px.bar(
        df,
        x="p_name",
        y="total_sales"
    )

    st.plotly_chart(fig, use_container_width=True)


customers = requests.get(
    f"{API}/analytics/top-customers"
).json()

if customers:

    df = pd.DataFrame(customers)

    st.subheader("Top Customers")

    fig = px.pie(
        df,
        names="name",
        values="total_orders"
    )

    st.plotly_chart(fig, use_container_width=True)


employees = requests.get(
    f"{API}/analytics/top-employees"
).json()

if employees:
    
    df = pd.DataFrame(employees)

    st.subheader("Top Employees")
    # st.write(employees)

    fig = px.bar(
        df,
        x="emp_name",
        y="total_orders"
    )

    st.plotly_chart(fig, use_container_width=True)


revenue = requests.get(
    f"{API}/analytics/category-revenue"
).json()

if revenue:

    df = pd.DataFrame(revenue)

    st.subheader("Revenue By Category")

    fig = px.bar(
        df,
        x="cat_name",
        y="revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

