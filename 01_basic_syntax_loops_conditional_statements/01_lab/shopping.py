budget = int(input())
total_cost = 0

while budget >= total_cost:
    command = input()
    if command == "End":
        print(f"You bought everything needed.")
        break

    total_cost += int(command)
else:
    print("You went in overdraft!")
