energy = int(input())
current_battle = 1
battles_won = 0

distance_to_enemy = input()
while distance_to_enemy != "End of battle":
    distance_to_enemy = int(distance_to_enemy)
    if battles_won % 3 == 0:
        energy += battles_won
    if energy >= distance_to_enemy:
        energy -= distance_to_enemy
        current_battle += 1
        battles_won += 1
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break
    distance_to_enemy = input()

else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
