def rating(dictionary: dict, plant_data: str):
    plant_data = plant_data.split(" - ")
    current_plant = plant_data[0]
    plant_rating = int(plant_data[1])

    if current_plant in dictionary.keys():
        dictionary[current_plant]["Rating"].append(plant_rating)
    else:
        print('error')
    return dictionary


def updating(dictionary: dict, plant_data: str):
    plant_data = plant_data.split(" - ")
    current_plant = plant_data[0]
    new_rarity = plant_data[1]

    if current_plant in dictionary.keys():
        dictionary[current_plant]["Rarity"] = new_rarity
    else:
        print('error')
    return dictionary


def resetting(dictionary: dict, plant_data: str):
    current_plant = plant_data
    if current_plant in dictionary.keys():
        dictionary[current_plant]["Rating"].clear()
    else:
        print('error')
    return dictionary


number_of_lines = int(input())
plant_dict = {}
for line in range(number_of_lines):
    plant, rarity = input().split("<->")
    if plant not in plant_dict.keys():
        plant_dict[plant] = {"Rarity": rarity,
                             "Rating": []
                             }
    else:
        plant_dict[plant]["Rarity"] = rarity

command = input()
while command != 'Exhibition':
    action, data = command.split(': ')
    if action == 'Rate':
        plant_dict = rating(plant_dict, data)
    elif action == 'Update':
        plant_dict = updating(plant_dict, data)
    elif action == 'Reset':
        plant_dict = resetting(plant_dict, data)
    command = input()

print(f'Plants for the exhibition:')

for name, plant_info in plant_dict.items():
    if len(plant_dict[name]["Rating"]) > 0:
        plant_average_rating = sum(plant_dict[name]["Rating"]) / len((plant_dict[name]["Rating"]))
    else:
        plant_average_rating = sum(plant_dict[name]["Rating"])
    plant_rarity = plant_dict[name]["Rarity"]

    print(f'- {name}; Rarity: {plant_rarity}; Rating: {plant_average_rating:.2f}')
