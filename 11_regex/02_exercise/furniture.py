import re

data = input()
pattern = rf">>([A-Za-z]+)<<(\d+(\.\d+)*)!(\d+)\b"
bought_items = []
total_cost = 0
while data != "Purchase":
    current_match = re.search(pattern, data)
    if current_match:
        item = current_match.group(1)
        price = current_match.group(2)
        amount = current_match.group(4)
        bought_items.append(item)
        total_cost += float(price) * int(amount)
    data = input()
print("Bought furniture:")
for item in bought_items:
    print(item)
print(f"Total money spend: {total_cost}")
