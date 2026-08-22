import streamlit as st

product_price = st.number_input("Enter the Price of Product")
discount = st.slider("Select Discount Percentage", 0,50,5)


if st.button("Final Price after Discount"):
    if product_price:
        final_price = product_price * (1-discount/100)
        st.success(f"{round(final_price, 2)}₹")

        st.table({
            "Product Price":[product_price],
            "Discount Percentage":[discount],
            "Final Price":[round(final_price, 2) if product_price else None]})
    else:
        st.warning("Enter the Product Price") 