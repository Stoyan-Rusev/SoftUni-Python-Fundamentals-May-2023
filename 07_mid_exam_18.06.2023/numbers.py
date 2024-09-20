def add(list_of_numbers, item):
    list_of_numbers.append(item)
    return list_of_numbers


def removing(list_of_numbers: list, item):
    if item in list_of_numbers:
        list_of_numbers.remove(item)
    return list_of_numbers


def replace(list_of_numbers: list, item,  item_two):
    if item in list_of_numbers:
        removed_index = list_of_numbers.index(item)
        removed_item = list_of_numbers.pop(removed_index)
        list_of_numbers.insert(removed_index, item_two)
    return list_of_numbers


def collapse(list_of_numbers, item):
    list_of_numbers = list(filter(lambda x: x >= item, list_of_numbers))
    return list_of_numbers


numbers = [int(number) for number in input().split(" ")]
command = input()
while command != "Finish":
    command = command.split(" ")
    action = command[0]

    if action == "Add":
        value = int(command[1])
        numbers = add(numbers, value)
    if action == "Remove":
        value = int(command[1])
        numbers = removing(numbers, value)
    if action == "Replace":
        value_one = int(command[1])
        value_two = int(command[2])
        numbers = replace(numbers, value_one, value_two)
    if action == "Collapse":
        value = int(command[1])
        numbers = collapse(numbers, value)
    command = input()
print(*numbers, sep=" ")
