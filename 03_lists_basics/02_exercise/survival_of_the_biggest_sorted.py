numbers_as_strings_list = input().split()
amount_of_nums_removed = int(input())
number_as_digits = []

for num in numbers_as_strings_list:
    number_as_digits.append(int(num))

number_as_digits = sorted(number_as_digits)
only_smallest_numbers = number_as_digits[:amount_of_nums_removed]

# working with strings for the final result
for current_number in only_smallest_numbers:
    numbers_as_strings_list.remove(str(current_number))
final_result = ', '.join(numbers_as_strings_list)

print(final_result)
