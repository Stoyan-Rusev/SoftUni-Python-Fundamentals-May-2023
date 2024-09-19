houses = [int(house) for house in input().split("@")]
command = input()
hearts_given = 2
index = 0
last_position = 0
while command != "Love!":
    command = command.split(" ")
    action = command[0]
    jump_range = int(command[1])
    if (index + jump_range) in range(len(houses)):
        index += jump_range
        if houses[index] > 0:
            houses[index] -= hearts_given
            if houses[index] == 0:
                print(f"Place {index} has Valentine's day.")

        else:
            print(f"Place {index} a already had Valentine's day.")
        last_position = index
    else:
        index = 0
        if houses[index] > 0:
            houses[index] -= hearts_given
            if houses[index] == 0:
                print(f"Place {index} has Valentine's day.")

        else:
            print(f"Place {index} already had Valentine's day.")
        last_position = index
    # print(houses)
    # print(f"Last position : {last_position}")

    command = input()
if sum(houses) == 0:
    print(f"Cupid's last position was {last_position}.")
    print("Mission was successful.")
else:
    failed_places = 0
    for place in houses:
        if place != 0:
            failed_places += 1
    print(f"Cupid's last position was {last_position}.")
    print(f"Cupid has failed {failed_places} places.")
