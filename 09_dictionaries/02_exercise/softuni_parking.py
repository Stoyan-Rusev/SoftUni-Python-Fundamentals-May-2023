number_of_actions = int(input())
actions_info_list = [input() for current_data in range(number_of_actions)]
registration_dict = {}

for data in actions_info_list:
    data = data.split()
    if len(data) == 2:    # case when unregister a person
        action, name = data[0], data[1]
        if name in registration_dict.keys():
            del registration_dict[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

    elif len(data) == 3:  # case when register a person
        action, name, registration_plate = data[0], data[1], data[2]
        if name not in registration_dict.keys():
            registration_dict[name] = registration_plate
            print(f"{name} registered {registration_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {registration_plate}")

for name, plate in registration_dict.items():
    print(f"{name} => {plate}")
