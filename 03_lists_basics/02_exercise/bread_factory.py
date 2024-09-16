list_events_and_values = input().split('|')
energy = 100
coins = 100

for event in list_events_and_values:
    current_event = event.split('-')
    event_type = current_event[0]
    value = int(current_event[1])
    if event_type == "rest":
        if value + energy > 100:
            gained_energy = value - (value + energy - 100)
            energy = 100
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        else:
            gained_energy = value
            energy += value
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")

    elif event_type == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event_type}.")
        else:
            coins -= value
            print(f"Closed! Cannot afford {event_type}.")
            break
if coins >= 0:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
