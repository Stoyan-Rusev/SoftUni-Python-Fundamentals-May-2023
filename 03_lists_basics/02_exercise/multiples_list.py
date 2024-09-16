factor = int(input())
count = int(input())
list_of_numbers = []

for number in range(1, count + 1):
    list_of_numbers.append(factor * number)

print(list_of_numbers)
