def collect(inventory: list, item: str) -> list:
    if item not in inventory:
        inventory.append(item)
    return inventory


def drop(inventory: list, item: str) -> list:
    if item in inventory:
        inventory.remove(item)
    return inventory


def combine_items(inventory: list, old, new) -> list:
    if old in inventory:
        index_old_item = inventory.index(old)
        inventory.insert(index_old_item + 1, new)
    return inventory


def renew(inventory: list, item: str) -> list:
    if item in inventory:
        item_index = inventory.index(item)
        removed_item = inventory.pop(item_index)
        inventory.append(removed_item)
    return inventory


my_inventory = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    action = command[0]

    if action == "Collect":
        current_item = command[1]
        my_inventory = collect(my_inventory, current_item)
    elif action == "Drop":
        current_item = command[1]
        my_inventory = drop(my_inventory, current_item)
    elif action == "Combine Items":
        old_and_new_items = command[1].split(":")
        old_item = old_and_new_items[0]
        new_item = old_and_new_items[1]
        my_inventory = combine_items(my_inventory, old_item, new_item)
    elif action == "Renew":
        current_item = command[1]
        my_inventory = renew(my_inventory, current_item)

    command = input()

print(*my_inventory, sep=", ")
