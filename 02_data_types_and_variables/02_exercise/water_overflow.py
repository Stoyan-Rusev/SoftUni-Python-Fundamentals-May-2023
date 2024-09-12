TANK_CAPACITY_L = 255
number_of_lines = int(input())
total_liters = 0

for _ in range(number_of_lines):
    liters_of_water_added = int(input())
    if liters_of_water_added + total_liters <= TANK_CAPACITY_L:
        total_liters += liters_of_water_added
    else:
        print('Insufficient capacity!')
print(total_liters)
 