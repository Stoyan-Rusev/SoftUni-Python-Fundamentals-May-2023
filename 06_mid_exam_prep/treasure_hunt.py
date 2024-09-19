def loot():
    pass


chest_storage = input().split("|")
while True:
    operation_and_items = input().split(" ")
    operation = operation_and_items[0]
    only_items = [item for item in operation_and_items if item != operation]

    if operation == "Yohoho!":
        break
    if operation == "Loot":
        for current_item in only_items:
            if current_item not in chest_storage:
                chest_storage.insert(0, current_item)
    elif operation == "Drop":
        index = only_items[0]
        # if index in range(len(chest_storage)):
        x = chest_storage.pop(0)
        chest_storage.append(x)
    elif operation == "Steal":
        number_of_stolen_items = int(only_items[0])
        if number_of_stolen_items >= len(chest_storage):
            print(", ".join(chest_storage))
            chest_storage.clear()
        else:
            print(", ".join(chest_storage[:-3]))
            chest_storage = chest_storage[:-3]

if len(chest_storage) <= 0:
    print(f"Failed treasure hunt.")
else:
    print(f"Average treasure gain: {sum([len(item) for item in chest_storage]):.2f} pirate credits.")

