items_with_prices_list = input().split('|')
budget = float(input())
ticket = 150
money_spent = 0
items_profit_string = ''

for items in items_with_prices_list:
    item = items.split("->")
    product = item[0]
    price = float(item[1])
    current_item_profit = ''

    if product == "Clothes" and price <= 50.00:
        budget -= price
        money_spent += price
        current_item_profit += str(price * 1.4)
        items_profit_string += f'{current_item_profit} '

    elif product == "Shoes" and price <= 35.00:
        budget -= price
        money_spent += price
        current_item_profit += str(price * 1.4)
        items_profit_string += f'{current_item_profit} '

    elif product == "Accessories" and price <= 20.50:
        budget -= price
        money_spent += price
        current_item_profit += str(price * 1.4)
        items_profit_string += f'{current_item_profit} '

print(items_profit_string)