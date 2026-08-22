import streamlit as st

st.title("Sales Info")
st.subheader("Simple Sales Dashboard")
selected_month = st.selectbox("Months", ["January", "February", "March", "April"])

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

st.metric("Sales", sales[selected_month]) 

chart_data = {"Month": list(sales.keys()), "Sales": list(sales.values())}
st.bar_chart(chart_data, x="Month", y="Sales")