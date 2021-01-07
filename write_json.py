import json
data = [
    {
        "sku": "WALMART-01",
        "name": "Frozen Rubber Chicken",
        "price" : 25
    },
    {
        "sku": "WALMART-02",
        "name": "Rubber Ball",
        "price" : 5
    },
    {
        "sku": "WALMART-03",
        "name": "Broom",
        "price" : 15
    }
]

with open("ecomm2.json", "w") as fileptr:
    json.dump(data, fileptr)