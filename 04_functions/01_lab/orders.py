def order_calculator(product, quantity):
    coffee_price = 1.50
    water_price = 1.00
    coke_price = 1.40
    snacks_price = 2.00
    total_cost = 0
    if product == "coffee":
        total_cost = coffee_price * quantity
    elif product == "water":
        total_cost = water_price * quantity
    elif product == "coke":
        total_cost = coke_price * quantity
    elif product == "snacks":
        total_cost = snacks_price * quantity
    return f'{total_cost:.2f}'


current_product = input()
current_quantity = int(input())
print(order_calculator(current_product, current_quantity))
