def cast_spelling(heroes_dictionary: dict, split_data: list):
    hero_name = split_data[1]
    mp_needed = int(split_data[2])
    spell_name = split_data[3]

    if heroes_dictionary[hero_name]["MP"] >= mp_needed:
        heroes_dictionary[hero_name]["MP"] -= mp_needed
        return f"{hero_name} has successfully cast {spell_name} and now has {heroes_dictionary[hero_name]['MP']} MP!"
    return f"{hero_name} does not have enough MP to cast {spell_name}!"


def taking_damage(heroes_dictionary: dict, split_data: list):
    hero_name = split_data[1]
    damage = int(split_data[2])
    enemy_name = split_data[3]

    if heroes_dictionary[hero_name]["HP"] > damage:
        heroes_dictionary[hero_name]["HP"] -= damage
        return f"{hero_name} was hit for {damage} HP by {enemy_name} and now has {heroes_dictionary[hero_name]['HP']} HP left!"
    del heroes_dictionary[hero_name]
    return f"{hero_name} has been killed by {enemy_name}!"


def recharging(heroes_dictionary: dict, split_data: list):
    hero_name = split_data[1]
    amount = int(split_data[2])

    if heroes_dictionary[hero_name]["MP"] + amount >= 200:
        amount_recovered = 200 - heroes_dictionary[hero_name]["MP"]
        heroes_dictionary[hero_name]["MP"] = 200
    else:
        amount_recovered = amount
        heroes_dictionary[hero_name]["MP"] = heroes_dictionary[hero_name]["MP"] + amount
    return f"{hero_name} recharged for {amount_recovered} MP!"


def healing(heroes_dictionary: dict, split_data: list):
    hero_name = split_data[1]
    amount = int(split_data[2])

    if heroes_dictionary[hero_name]["HP"] + amount >= 100:
        amount_recovered = 100 - heroes_dictionary[hero_name]["HP"]
        heroes_dictionary[hero_name]["HP"] = 100
    else:
        amount_recovered = amount
        heroes_dictionary[hero_name]["HP"] = heroes_dictionary[hero_name]["HP"] + amount
    return f"{hero_name} healed for {amount_recovered} HP!"


number_of_heroes = int(input())
heroes_dict = {}

for current_num in range(number_of_heroes):
    current_hero_data = input().split(" ")
    name = current_hero_data[0]
    hit_points = int(current_hero_data[1])
    mana_points = int(current_hero_data[2])
    heroes_dict[name] = {"HP": hit_points,
                         "MP": mana_points}

command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        print(cast_spelling(heroes_dict, command))
    elif action == "TakeDamage":
        print(taking_damage(heroes_dict, command))
    elif action == "Recharge":
        print(recharging(heroes_dict, command))
    elif action == "Heal":
        print(healing(heroes_dict, command))

    command = input()

for hero, values in heroes_dict.items():
    print(hero)
    print(f"HP: {heroes_dict[hero]['HP']}")
    print(f"MP: {heroes_dict[hero]['MP']}")
