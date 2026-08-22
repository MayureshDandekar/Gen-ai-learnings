prices = [100,250,400,1200,50]

gst = map(lambda x: x * (1+0.18), prices)
prices_with_gst = list(gst)
print(f"prices are {prices}\nprices after adding gst are {prices_with_gst}")