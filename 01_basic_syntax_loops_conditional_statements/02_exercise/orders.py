number_of_orders = int(input())
price = 0
total = 0

for order_num in range(number_of_orders):
    price_per_capsule = float(input())
    days = float(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price = price_per_capsule * days * capsules_per_day
    total += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total:.2f}")
