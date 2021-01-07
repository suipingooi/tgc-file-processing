cost_table = {
    "apple" : 0.5,
    "orange" : 0.7,
    "pineapple" : 1, 
    "watermelon" : 2.5,
    "durian" : 10,
}

print(cost_table["watermelon"])

with open("fruits.txt") as fileptr:
    total_cost = 0
    count = 0
    for fruit in fileptr:
        fruit = fruit.strip().lower()
        print(fruit)
        total_cost += cost_table[fruit]
    print("total cost = ", total_cost)
        