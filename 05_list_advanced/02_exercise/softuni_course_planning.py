schedule = input().split(', ')
while True:
    command = input()
    if command == 'course start':
        break

    command = command.split(':')
    operation = command[0]
    item = command[1]

    if operation == 'Add':
        if item not in schedule:
            schedule.append(item)
    elif operation == 'Insert':
        index = int(command[2])
        if item not in schedule:
            schedule.insert(index, item)
    elif operation == 'Remove':
        if item in schedule:
            index = schedule.index(item)
            if schedule[index + 1] == f"{item}-Exercise":
                exercise = schedule[index + 1]
                schedule.remove(exercise)
                schedule.remove(item)
            else:
                schedule.remove(item)
    elif operation == 'Swap':
        item_two = command[2]
        index_item_one = schedule.index(item)
        index_item_two = schedule.index(item_two)

        if item in schedule and item_two in schedule:
            schedule[index_item_one], schedule[index_item_two] = schedule[index_item_two], schedule[index_item_one]
            if "Exercise" in schedule[index_item_one + 1] and "Exercise" not in schedule[index_item_two + 1]:
                schedule.remove(f"{item}-Exercise")
                schedule.insert(index_item_two + 1, f"{item}-Exercise")
            elif "Exercise" in schedule[index_item_two + 1] and "Exercise" not in schedule[index_item_one + 1]:
                schedule.remove(f"{item_two}-Exercise")
                schedule.insert(index_item_one + 1, f"{item_two}-Exercise")
            elif "Exercise" in schedule[index_item_one + 1] and "Exercise" in schedule[index_item_two + 1]:
                schedule[index_item_one + 1], schedule[index_item_two + 1] = \
                    schedule[index_item_two + 1], schedule[index_item_one + 1]

    elif operation == 'Exercise':
        if item in schedule:
            lab_index = schedule.index(item)
            schedule.insert(lab_index + 1, f"{item}-Exercise")
        else:
            schedule.append(item)
            schedule.append(f"{item}-Exercise")

number = 1
for item in schedule:
    print(f'{number}.{item}')
    number += 1
