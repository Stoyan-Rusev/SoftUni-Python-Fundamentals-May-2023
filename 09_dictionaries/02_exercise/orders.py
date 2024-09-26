orders = {}
current_order = input().split()

while current_order[0] != 'buy':
    product, price, quantity = current_order[0], float(current_order[1]), int(current_order[2])
    if product not in orders.keys():
        orders[product] = [price, quantity]
    elif product in orders.keys():
        orders[product][0] = price
        orders[product][1] += quantity

    current_order = input().split()

for current_product in orders.keys():
    total_price = f"{orders[current_product][0] * orders[current_product][1]:.2f}"
    print(f"{current_product} -> {total_price}")
