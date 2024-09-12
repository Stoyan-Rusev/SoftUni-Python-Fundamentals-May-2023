snowballs_made = int(input())
value = 0
highest_value = 0
highest_weight = 0
highest_time_needed = 0
highest_quality = 0

for snowball in range(1, snowballs_made + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = int((weight / time_needed) ** quality)

    if value > highest_value:
        highest_value = value
        highest_weight = weight
        highest_time_needed = time_needed
        highest_quality = quality

print(f"{highest_weight} : {highest_time_needed} = {highest_value} ({highest_quality})")
