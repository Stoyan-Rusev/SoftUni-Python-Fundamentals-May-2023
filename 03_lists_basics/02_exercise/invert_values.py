list_of_numbers = input().split()
reversed_list = []

for index in range(len(list_of_numbers)):
    invert_number = -int(list_of_numbers[index])
    reversed_list.append(invert_number)

print(reversed_list)
