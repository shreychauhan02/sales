import streamlit as st

st.set_page_config(
    page_title="Sales Management System",

    layout="wide"
)

st.title(" Sales Management Dashboard")

st.markdown("""
### Welcome

Use the sidebar to navigate:

- Dashboard
- Customers
- Products
- Employees
- Orders

Built with:
- FastAPI
- Streamlit
- MySQL
- Plotly
""")