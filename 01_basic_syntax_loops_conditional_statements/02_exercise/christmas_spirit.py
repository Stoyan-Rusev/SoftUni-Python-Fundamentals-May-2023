quantity_of_decorations = int(input())
days_to_christmas = int(input())
money_counter = 0
spirit = 0

ornament_price = 2
ornament_points = 5
skirt_price = 5
skirt_points = 3
garland_price = 3
garland_points = 10
lights_price = 15
lights_points = 17

for day in range(1, days_to_christmas + 1):
    if day == 11:
        quantity_of_decorations += 2
    if day % 2 == 0:
        money_counter += ornament_price * quantity_of_decorations
        spirit += ornament_points
    if day % 3 == 0:
        money_counter += skirt_price * quantity_of_decorations + garland_price * quantity_of_decorations
        spirit += skirt_points + garland_points
    if day % 5 == 0:
        money_counter += lights_price * quantity_of_decorations
        spirit += lights_points
    if day % 10 == 0:
        spirit -= 20
        money_counter += skirt_price + garland_price + lights_price

if days_to_christmas % 10 == 0:
    spirit -= 30
print(f"Total cost: {money_counter}\nTotal spirit: {spirit}")
