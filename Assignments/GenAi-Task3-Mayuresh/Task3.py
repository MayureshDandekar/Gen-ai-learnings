gst = lambda price: price *(1+0.18)
# print(f"total amount after adding gst is {gst(100)}")
gst_price = gst(100)
print(gst_price)

discount_percent = 5
final_price = lambda price : (price +(0.18*price)) * (1-discount_percent/100)
print(final_price(100))


