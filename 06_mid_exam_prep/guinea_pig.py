food_for_month = float(input())
hay_for_month = float(input())
cover_for_month = float(input())
pig_weight = float(input())

for day in range(1, 30 + 1):
    food_for_month -= 0.300
    if day % 2 == 0:
        hay_for_month -= 0.05 * food_for_month
    if day % 3 == 0:
        cover_for_month -= (1 / 3) * pig_weight
    if food_for_month <= 0 or cover_for_month <= 0 or hay_for_month <= 0:
        print(f"Merry must go to the pet store!")
        break
if food_for_month > 0 and hay_for_month > 0 and cover_for_month > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_for_month:.2f}, Hay: {hay_for_month:.2f}"
          f", Cover: {cover_for_month:.2f}.")
