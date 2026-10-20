"""iPhone 13 Again"""
phone = input()
storage = input()
price = 0

if phone == "iPhone 13 mini":
    if storage == "128 GB":
        price = 25900
    elif storage == "256 GB":
        price = 29900
    elif storage == "512 GB":
        price = 37900

elif phone == "iPhone 13":
    if storage == "128 GB":
        price = 29900
    elif storage == "256 GB":
        price = 33900
    elif storage == "512 GB":
        price = 41900

elif phone == "iPhone 13 Pro":
    if storage == "128 GB":
        price = 38900
    elif storage == "256 GB":
        price = 42900
    elif storage == "512 GB":
        price = 50900
    elif storage == "1 TB":
        price = 58900

elif phone == "iPhone 13 Pro Max":
    if storage == "128 GB":
        price = 42900
    elif storage == "256 GB":
        price = 46900
    elif storage == "512 GB":
        price = 54900
    elif storage == "1 TB":
        price = 62900

if not price:
    print("Not Available")
else:
    print(price)
