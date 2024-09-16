def sum_numbers(num_one, num_two):
    return num_one + num_two


def subtract(sum_of_two_numbers, num_three):
    return sum_of_two_numbers - num_three


def add_and_subtract(first_num, second_num, third_num):
    sum_of_first_num_and_second_num = sum_numbers(first_num, second_num)
    result = subtract(sum_of_first_num_and_second_num, third_num)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
