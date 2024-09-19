def shoot(list_of_targets, target_index, shooting_power):
    if target_index in range(len(list_of_targets)):
        if shooting_power >= list_of_targets[target_index]:
            list_of_targets.remove(list_of_targets[target_index])
        else:
            list_of_targets[target_index] -= shooting_power
    return list_of_targets


def add(list_of_targets, target_index, value):
    if target_index in range(len(list_of_targets)):
        list_of_targets.insert(target_index, value)
    else:
        print("Invalid placement!")
    return list_of_targets


def strike(list_of_targets, target_index, striking_radius):
    if target_index - striking_radius not in range(len(list_of_targets)) or \
            target_index + striking_radius not in range(len(list_of_targets)):
        print("Strike missed!")
    else:
        list_of_targets = list_of_targets[0:target_index - striking_radius] \
            + list_of_targets[target_index + striking_radius + 1:]
    return list_of_targets


targets = [int(target) for target in input().split(" ")]

command = input()
while command != "End":
    command = command.split(" ")
    action = command[0]
    index = int(command[1])

    if action == "Shoot":
        power = int(command[2])
        targets = shoot(targets, index, power)
    elif action == "Add":
        target_value = int(command[2])
        targets = add(targets, index, target_value)
    elif action == "Strike":
        radius = int(command[2])
        targets = strike(targets, index, radius)
    command = input()
print(*targets, sep="|")
