needed_experience = float(input())
number_of_battles = int(input())
total_experience = 0

for current_battle in range(1, number_of_battles + 1):
    xp_earned = float(input())
    if current_battle % 15 == 0:
        bonus_xp = 0.05 * xp_earned
        total_experience += (xp_earned + bonus_xp)
    elif current_battle % 3 == 0:
        bonus_xp = 0.15 * xp_earned
        total_experience += (xp_earned + bonus_xp)
    elif current_battle % 5 == 0:
        xp_taken = 0.10 * xp_earned
        total_experience += (xp_earned - xp_taken)
    else:
        total_experience += xp_earned
    if total_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {current_battle} battles.")
        break
else:
    print(f"Player was not able to collect the needed experience, {needed_experience - total_experience:.2f} more needed.")
