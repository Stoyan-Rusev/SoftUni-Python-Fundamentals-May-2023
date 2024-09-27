import re

text = input()
pattern = r'([|#])([A-Za-z ]+)\1([\d]{2}/[\d]{2}/[\d]{2})\1(\d+)\1'
matches = re.findall(pattern, text)
needed_calories_per_day = 2000
total_food_calories = 0
list_with_food_data = []

for current_match in matches:
    product = current_match[1]
    expiration_date = current_match[2]
    calories = int(current_match[3])
    list_with_food_data.append(f"Item: {product}, Best before: {expiration_date}, Nutrition: {calories}")
    total_food_calories += calories

days = total_food_calories // needed_calories_per_day
print(f"You have food to last you for: {days} days!")
if days > 0:
    for current_item in list_with_food_data:
        print(current_item)
