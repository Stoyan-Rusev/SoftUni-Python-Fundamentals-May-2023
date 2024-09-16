employees_list = [int(employee) for employee in input().split()]
happiness_factor = int(input())

employees_happiness = [employee * happiness_factor for employee in employees_list]
happy_count = 0

for current_happiness in employees_happiness:
    if current_happiness >= sum(employees_happiness) / len(employees_happiness):
        happy_count += 1
if happy_count >= len(employees_list) // 2:
    print(f"Score: {happy_count}/{len(employees_list)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(employees_list)}. Employees are not happy!")
