def driving(car_dict: dict, parameters: list):
    car = parameters[0]
    distance = int(parameters[1])
    fuel_needed = int(parameters[2])

    if car_dict[car]['Fuel'] >= fuel_needed:
        car_dict[car]['Mileage'] += distance
        car_dict[car]['Fuel'] -= fuel_needed
        print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
    elif car_dict[car]['Fuel'] < fuel_needed:
        print("Not enough fuel to make that ride")
    if car_dict[car]['Mileage'] >= 100000:
        print(f"Time to sell the {car}!")
        del car_dict[car]
    return car_dict


def refueling(car_dict: dict, parameters: list):
    car = parameters[0]
    fuel = int(parameters[1])
    tank_capacity = 75

    if car_dict[car]['Fuel'] + fuel >= tank_capacity:
        print(f"{car} refueled with {tank_capacity - car_dict[car]['Fuel'] } liters")
        car_dict[car]['Fuel'] = tank_capacity
    else:
        print(f"{car} refueled with {fuel} liters")
        car_dict[car]['Fuel'] += fuel
    return car_dict


def reverting(car_dict: dict, parameters: list):
    car = parameters[0]
    kilometers = int(parameters[1])

    if car_dict[car]['Mileage'] - kilometers < 10000:
        car_dict[car]['Mileage'] = 10000
    else:
        car_dict[car]['Mileage'] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return car_dict


number_of_cars = int(input())
garage_dictionary = {}
for line in range(number_of_cars):
    cars_with_info = input().split("|")
    current_car = cars_with_info[0]
    initial_mileage = int(cars_with_info[1])
    initial_fuel = int(cars_with_info[2])

    if current_car not in garage_dictionary.keys():
        garage_dictionary[current_car] = {"Mileage": initial_mileage,
                                          'Fuel': initial_fuel}

command = input()
while command != 'Stop':
    action, *params = command.split(" : ")
    if action == 'Drive':
        garage_dictionary = driving(garage_dictionary, params)
    elif action == 'Refuel':
        garage_dictionary = refueling(garage_dictionary, params)
    elif action == 'Revert':
        garage_dictionary = reverting(garage_dictionary, params)
    command = input()

for car, info in garage_dictionary.items():
    print(f"{car} -> Mileage: {garage_dictionary[car]['Mileage']} kms, Fuel in the tank: {garage_dictionary[car]['Fuel']} lt.")
