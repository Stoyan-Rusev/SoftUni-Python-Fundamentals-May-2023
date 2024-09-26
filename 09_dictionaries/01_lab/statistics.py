data = input().split(": ")
stash = {}
while data[0] != "statistics":
    product = data[0]
    quantity = int(data[1])
    if product not in stash.keys():
        stash[product] = quantity
    else:
        stash[product] += quantity

    data = input().split(": ")

print("Products in stock:")
for current_product in stash.keys():
    print(f"- {current_product}: {stash[current_product]}")
print(f"Total Products: {len(stash.keys())}")
print(f"Total Quantity: {sum(num for num in stash.values())}")
