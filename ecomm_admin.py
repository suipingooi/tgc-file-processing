import json

data = []

while True: 
    choice = input("Do you want to enter a new product (y/n)? ")
    if choice == "n":
        break
    sku = input("Please enter SKU of the product >")
    name = input("Please enter name of the product >")
    price = float(input("Please enter price of the product >"))
    data.append({
        "sku": sku,
        "name": name,
        "price": price
    })