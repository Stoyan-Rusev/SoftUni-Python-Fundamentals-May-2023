numbers_as_strings = input().split()
amount_of_nums_removed = int(input())
numbers_as_digits = []
final_result_as_list = []
final_result = ''

for number in numbers_as_strings:
    numbers_as_digits.append(int(number))

for _ in range(amount_of_nums_removed):
    smallest_number = numbers_as_digits[0]
    for num in numbers_as_digits:
        if num < smallest_number:
            smallest_number = num
    numbers_as_digits.remove(smallest_number)

for item in numbers_as_digits:
    final_result_as_list.append(str(item))

final_result = ', '.join(final_result_as_list)

print(final_result)
