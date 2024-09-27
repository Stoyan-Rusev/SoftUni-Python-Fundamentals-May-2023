def adding_animals(animals_dict: dict, animals_info: str):
    animals_info = animals_info.split('-')
    animal_name = animals_info[0]
    needed_food = int(animals_info[1])
    if animal_name not in animals_dict.keys():
        animals_dict[animal_name] = needed_food
    else:
        animals_dict[animal_name] += needed_food
    return animals_dict


def updating_area(areas_dict: dict, animals_info: str):
    animals_info = animals_info.split('-')
    animal_name = animals_info[0]
    area = animals_info[2]
    if area not in areas_dict.keys():
        areas_dict[area] = []
    if animal_name not in areas_dict[area]:
        areas_dict[area].append(animal_name)
    return areas_dict


def feeding(animals_dict: dict, animals_info: str):
    animals_info = animals_info.split('-')
    animal_name = animals_info[0]
    food = int(animals_info[1])
    if animal_name in animals_dict.keys():
        animals_dict[animal_name] -= food
    if animals_dict[animal_name] <= 0:
        del animals_dict[animal_name]
        print(f'{animal_name} was successfully fed')
    return animals_dict


def deleting_from_area(areas_dict: dict, animals_dict: dict, animals_info: str):
    animals_info = animals_info.split('-')
    animal_name = animals_info[0]
    if animal_name not in animals_dict.keys():
        for area, list_with_animals in areas_dict.items():
            if animal_name in list_with_animals:
                areas_dict[area].remove(animal_name)
    return areas_dict


command = input()
animals = {}
areas = {}

while command != 'EndDay':
    action, info = command.split(': ')
    if action == 'Add':
        animals = adding_animals(animals, info)
        areas = updating_area(areas, info)

    elif action == 'Feed':
        animals = feeding(animals, info)
        areas = deleting_from_area(areas, animals, info)

    command = input()

print('Animals:')
for animal_name, needed_food_quantity in animals.items():
    print(f' {animal_name} -> {needed_food_quantity}g')

print('Areas with hungry animals:')
for area_name, area_list_with_animals in areas.items():
    if areas[area_name]:
        print(f'{area_name}: {len(area_list_with_animals)}')
