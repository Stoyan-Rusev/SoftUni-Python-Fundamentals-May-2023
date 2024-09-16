items_with_prices_list = input().split("|")
budget = float(input())
TRAIN_TICKET = 150
items_selling_prices = []
total_selling_price = 0
total_buying_price = 0

for items in items_with_prices_list:
    product, price = items.split('->')
    price = float(price)
    if budget - price < 0:
        break

    if product == 'Clothes' and price <= 50.00:
        budget -= price
        items_selling_prices.append(f'{1.4 * price:.2f}')
        total_buying_price += price
    elif product == 'Shoes' and price <= 35.00:
        budget -= price
        items_selling_prices.append(f'{1.4 * price:.2f}')
        total_buying_price += price
    elif product == 'Accessories' and price <= 20.50:
        budget -= price
        items_selling_prices.append(f'{1.4 * price:.2f}')
        total_buying_price += price

for current_item_plus_profit in items_selling_prices:
    total_selling_price += float(current_item_plus_profit)
string_of_item_selling_prices = " ".join(items_selling_prices)

print(string_of_item_selling_prices)
print(f'Profit: {total_selling_price - total_buying_price:.2f}')
if total_selling_price + budget >= TRAIN_TICKET:
    print('Hello, France!')
else:
    print('Not enough money.')
