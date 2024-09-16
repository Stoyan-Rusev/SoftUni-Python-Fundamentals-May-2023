number_of_electrons = int(input())
shells = []
current_shell_number = 1
while number_of_electrons > 0:
    electrons_amount = 2 * current_shell_number ** 2
    if number_of_electrons >= electrons_amount:
        shells.append(electrons_amount)
        current_shell_number += 1
        number_of_electrons -= electrons_amount
    else:
        last_shell_amount = number_of_electrons
        shells.append(last_shell_amount)
        number_of_electrons = 0
print(shells)
