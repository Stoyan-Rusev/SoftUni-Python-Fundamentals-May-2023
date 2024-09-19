def delivering_hearts(list_of_houses: list, range_of_jump: int):
    hearts_delivered = 2
    for house_index, current_house in enumerate(list_of_houses):
        # if (house_index + range_of_jump) not in range(len(list_of_houses)):
        if current_house == 0:
            print(f"Place {house_index} already had Valentine's day.")
        else:
            list_of_houses[house_index] -= hearts_delivered
            if list_of_houses[house_index] == 0:
                print(f"Place {house_index} has Valentine's day.")
    return list_of_houses


houses = [int(house) for house in input().split("@")]
command = input()

while command != "Love":
    command = command.split(" ")
    action = command[0]
    jump_range = int(command[1])
    if action == "Jump":
        houses = delivering_hearts(houses,jump_range)
    print(houses)
    command = input()


