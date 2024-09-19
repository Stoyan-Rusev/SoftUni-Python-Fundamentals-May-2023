def urgent(list_with_groceries: list, item):
    if item not in list_with_groceries:
        list_with_groceries.insert(0, item)
    return list_with_groceries


def unnecessary(list_with_groceries: list, item):
    if item in list_with_groceries:
        list_with_groceries.remove(item)
    return list_with_groceries


def correct(list_with_groceries: list, old_item, new_item):
    if old_item in list_with_groceries:
        old_item_index = list_with_groceries.index(old_item)
        list_with_groceries.remove(old_item)
        list_with_groceries.insert(old_item_index, new_item)
    return list_with_groceries


def rearrange(list_with_groceries: list, item):
    if item in list_with_groceries:
        removed_item_index = list_with_groceries.index(item)
        removed_item = list_with_groceries.pop(removed_item_index)
        list_with_groceries.append(removed_item)
    return list_with_groceries


groceries = input().split("!")
command = input()
while command != "Go Shopping!":
    command = command.split(" ")
    current_action = command[0]
    current_item = command[1]

    if current_action == "Urgent":
        groceries = urgent(groceries, current_item)
    elif current_action == "Unnecessary":
        groceries = unnecessary(groceries, current_item)
    elif current_action == "Correct":
        current_new_item = command[2]
        groceries = correct(groceries, current_item, current_new_item)
    elif current_action == "Rearrange":
        groceries = rearrange(groceries, current_item)

    command = input()

print(", ".join(groceries))
