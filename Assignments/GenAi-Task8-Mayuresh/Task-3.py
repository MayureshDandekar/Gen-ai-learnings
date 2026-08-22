import streamlit as st

product_name = st.sidebar.text_input("Enter The Name of Product")
product_category = st.sidebar.selectbox("Category", ["Electronic","Furniture","Home Appliance"])
product_price = st.sidebar.number_input("Enter the Price of Product")

if st.sidebar.button("Add Product"):
    if product_name and product_price:
        st.sidebar.success("Your Product is Added Successfully")
        st.table({"Product Name": [product_name],
                  "Product Category": [product_category],
                  "Product Price": [product_price]})
    else:
        st.sidebar.warning("Enter the Product Details")