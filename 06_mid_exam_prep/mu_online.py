INITIAL_HEALTH = 100

bitcoins = 0
current_health = INITIAL_HEALTH
last_room = 0

rooms_with_values = input().split("|")
for room_index, current_room in enumerate(rooms_with_values):
    current_room = current_room.split(" ")
    command = current_room[0]
    value = int(current_room[1])

    if command == "potion":

        if current_health + value >= INITIAL_HEALTH:
            healed_by = INITIAL_HEALTH - current_health
            current_health = INITIAL_HEALTH
            print(f"You healed for {healed_by} hp.")
        else:
            current_health += value
            print(f"You healed for {value} hp.")
        print(f"Current health: {current_health} hp.")

    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        current_health -= value
        if current_health <= 0:
            last_room = room_index + 1
            print(f"You died! Killed by {command}.")
            break
        else:
            print(f"You slayed {command}.")


if current_health <= 0:
    print(f"Best room: {last_room}")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")
