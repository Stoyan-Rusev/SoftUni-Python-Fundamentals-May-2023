def loot(chest_with_loots, items):
    for item in items:
        if item not in chest_with_loots:
            chest_with_loots.insert(0, item)
    return chest_with_loots


def drop(chest_with_loots, dropping_index):
    if dropping_index in range(len(chest_with_loots)):
        dropped_item = chest_with_loots.pop(dropping_index)
        chest_with_loots.append(dropped_item)
    return chest_with_loots


def steal(chest_with_loots, count_stolen):
    if count_stolen >= len(chest_with_loots):
        print(", ".join(chest_with_loots))
        chest_with_loots = chest_with_loots.clear()
    else:
        print(", ".join(chest_with_loots[-3:]))
        chest_with_loots = chest_with_loots[:-count_stolen]
    return chest_with_loots


treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split(" ")
    action = command[0]
    if action == "Loot":
        loots = command[1:]
        treasure_chest = loot(treasure_chest, loots)

    elif action == "Drop":
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)

    elif action == "Steal":
        amount_of_items_stolen = int(command[1])
        treasure_chest = steal(treasure_chest, amount_of_items_stolen)
    command = input()

if not treasure_chest:
    print("Failed treasure hunt.")
else:
    sum_of_all = 0
    for current_item in treasure_chest:
        sum_of_all += len(current_item)
    print(f"Average treasure gain: {sum_of_all / len(treasure_chest):.2f} pirate credits.")
